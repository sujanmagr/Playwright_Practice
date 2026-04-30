from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False, slow_mo=5000)

    page=browser.new_page()

    page.goto("https://formy-project.herokuapp.com/form")

    page.get_by_label("First name").fill("Sachin")

    page.get_by_label("Last name").fill("Budhathoki")
    page.get_by_label("Job title").fill("Full Stack Developer")

    page.locator("#radio-button-2").check()
    page.locator("#checkbox-2").check()

    page.get_by_label("Years of experience:").select_option(label="0-1")

    page.get_by_label("Date").fill("22/03/2026")

    page.get_by_role("button", name="Submit").click()

    browser.close()


    