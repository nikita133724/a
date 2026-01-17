
from playwright.sync_api import sync_playwright
import os

url = os.environ.get("TARGET_URL", "https://csgoyz.run/raffles")  # URL берём из переменной окружения

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url, wait_until="networkidle")
    html = page.content()
    browser.close()

print("[HTML]:", html)  # вывод в логи Render