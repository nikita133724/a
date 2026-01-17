from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Запускаем Chromium без UI (headless)
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    url = "https://csgoyz.run/raffles"
    page.goto(url, wait_until="networkidle")  # Ждём рендер JS

    # Сохраняем HTML в файл
    html = page.content()
    with open("page.html", "w", encoding="utf-8") as f:
        f.write(html)

    browser.close()
    print("HTML сохранён в page.html")