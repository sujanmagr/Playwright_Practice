import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://formy-project.herokuapp.com/form")
    page.locator("html").click()
    page.get_by_role("textbox", name="First name").click()
    page.get_by_role("textbox", name="First name").fill("sachin")
    page.get_by_role("textbox", name="Last name").click()
    page.get_by_role("textbox", name="Last name").fill("budhathoki")
    page.get_by_role("textbox", name="Job title").click()
    page.get_by_role("textbox", name="Job title").fill("full stack dev")
    page.locator("#radio-button-2").check()
    page.locator("#checkbox-2").check()
    page.get_by_label("Years of experience:").select_option("3")
    page.get_by_role("textbox", name="mm/dd/yyyy").click()
    page.get_by_role("textbox", name="mm/dd/yyyy").fill("02/22/2026")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_role("heading")).to_contain_text("Thanks for submitting your form")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


