
from playwright.sync_api import sync_playwright
import os

url = os.environ.get("TARGET_URL", "https://csgoyz.run/raffles")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url, wait_until="networkidle")
    page.wait_for_timeout(5000)  # ждём 5 секунд для выполнения JS
    html = page.content()
    browser.close()

print("[HTML]:", html)