from requests_html import HTMLSession
from pathlib import Path

URL = "https://csgoyz.run/raffles"
OUT_FILE = Path("raffles_dom.html")

session = HTMLSession()
r = session.get(URL)
r.html.render(sleep=3, keep_page=False)  # JS выполнится
OUT_FILE.write_text(r.html.html, encoding="utf-8")
print(f"[OK] HTML saved to {OUT_FILE.resolve()}")