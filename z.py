import requests
from pathlib import Path

URL = "https://csgoyz.run/raffles"
OUT_FILE = Path("raffles_dom.html")

r = requests.get(URL)
OUT_FILE.write_text(r.text, encoding="utf-8")
print(f"[OK] HTML saved to {OUT_FILE.resolve()}")