from requests_html import HTMLSession
from pathlib import Path

URL = "https://csgoyz.run/raffles"
OUT_FILE = Path("raffles_dom.html")

session = HTMLSession()

print(f"[INFO] Fetching {URL} ...")
r = session.get(URL)

# Headless JS render (если нужна динамика)
print("[INFO] Rendering JS (headless)...")
r.html.render(sleep=3, keep_page=False)

# Сохраняем HTML
OUT_FILE.write_text(r.html.html, encoding="utf-8")
print(f"[OK] HTML saved to {OUT_FILE.resolve()}")