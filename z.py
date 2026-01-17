from playwright.sync_api import sync_playwright

url = "https://example.com"  # сюда вставь нужный сайт

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # без окна
    page = browser.new_page()
    page.goto(url, wait_until="networkidle")  # ждём выполнения JS
    html = page.content()  # финальный HTML
    browser.close()

print(html)  # выводим HTML в логи