# # first paywright code
# import re
# from playwright.sync_api import Page, expect

# def test_has_title(page: Page):
#     page.goto("https://playwright.dev/")

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Playwright"))

# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")

#     # Click the get started link.
#     page.get_by_role("link", name="get started").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()

from playwright.sync_api import sync_playwright
# Start Playwright engine
with sync_playwright() as p:
 # Launch browser (Chromium)
    browser = p.chromium.launch(headless=False)
 # Open a new browser page
    page = browser.new_page()
 # Navigate to the website
    page.goto("https://www.saucedemo.com/")
 # Click link using text locator
    page.get_by_placeholder("Username").fill("standard_user")
    #send password
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
 # Close the browser
    browser.close()
# # # To Run: pytest --headed --slowmo 500

# import re
# from playwright.sync_api import Playwright, sync_playwright, expect

# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.saucedemo.com/")
#     page.locator("[data-test=\"username\"]").click()
#     page.locator("[data-test=\"username\"]").fill("standard_user")
#     page.locator("[data-test=\"password\"]").click()
#     page.locator("[data-test=\"password\"]").fill("secret_sauce")
#     page.locator("[data-test=\"login-button\"]").click()

#     # ---------------------
#     context.close()
#     browser.close()

# with sync_playwright() as playwright:
#     run(playwright)

# page.evaluate("window.scrollBy(0,100)")