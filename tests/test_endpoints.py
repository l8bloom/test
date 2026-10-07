import re
from html.parser import HTMLParser

from fastapi.testclient import TestClient

from health_service.main import app


client = TestClient(app)


class EndpointsTableParser(HTMLParser):
    """Collect the document title, the <th> headers, and the <td> rows, in order."""

    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.headers: list[str] = []
        self.rows: list[list[str]] = []
        self._in_title = False
        self._section: str | None = None
        self._cell: str | None = None
        self._row: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag == "title":
            self._in_title = True
        elif tag in ("thead", "tbody"):
            self._section = tag
        elif tag == "tr":
            self._row = []
        elif tag in ("th", "td"):
            self._cell = ""

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        elif tag in ("thead", "tbody"):
            self._section = None
        elif tag in ("th", "td"):
            assert self._cell is not None
            self._row.append(self._cell.strip())
            self._cell = None
        elif tag == "tr":
            if self._section == "thead" and self._row:
                self.headers = self._row
            elif self._section == "tbody" and self._row:
                self.rows.append(self._row)
            self._row = []

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data
        elif self._cell is not None:
            self._cell += data


def _parse(html: str) -> EndpointsTableParser:
    parser = EndpointsTableParser()
    parser.feed(html)
    return parser


def test_endpoints_returns_html_page() -> None:
    response = client.get("/endpoints")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    parsed = _parse(response.text)
    assert parsed.title == "Service endpoints"


def test_endpoints_table_headers() -> None:
    parsed = _parse(client.get("/endpoints").text)

    assert parsed.headers == ["Path", "Verb", "Owner", "On call"]


def test_endpoints_table_rows() -> None:
    parsed = _parse(client.get("/endpoints").text)

    assert parsed.rows == [
        ["/hello", "GET", "Team Kestrel", "Weekdays"],
        ["/health", "GET", "Team Osprey", "Always"],
        ["/goodbye", "GET", "Team Heron", "Weekends"],
    ]


def test_endpoints_header_row_colours() -> None:
    html = client.get("/endpoints").text

    style = re.search(r"<style>(.*?)</style>", html, re.DOTALL).group(1)
    header_rule = re.search(r"thead\s+th\s*{(.*?)}", style, re.DOTALL).group(1)
    background = (
        re.search(r"background(?:-color)?:\s*(#[0-9a-fA-F]{6})", header_rule)
        .group(1)
    )
    colour = re.search(r"(?<![a-z-])color:\s*(#[0-9a-fA-F]{6})", header_rule).group(1)

    def channels(hex_value: str) -> tuple[int, int, int]:
        value = int(hex_value.lstrip("#"), 16)
        return (value >> 16) & 0xFF, (value >> 8) & 0xFF, value & 0xFF

    # The mockup header row is #2e7d5b with #ffffff text.
    background_rgb = channels(background)
    assert all(
        abs(a - b) <= 16 for a, b in zip(background_rgb, (46, 125, 91))
    )
    assert channels(colour) == (255, 255, 255)


def test_endpoints_rejects_post() -> None:
    response = client.post("/endpoints")

    assert response.status_code == 405
