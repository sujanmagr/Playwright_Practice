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
#     page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
#     page.locator("[data-test=\"shopping-cart-link\"]").click()
#     page.locator("[data-test=\"checkout\"]").click()
#     page.locator("[data-test=\"firstName\"]").click()
#     page.locator("[data-test=\"firstName\"]").fill("test")
#     page.locator("[data-test=\"lastName\"]").click()
#     page.locator("[data-test=\"lastName\"]").fill("sachin")
#     page.locator("[data-test=\"postalCode\"]").click()
#     page.locator("[data-test=\"postalCode\"]").fill("123")
#     page.locator("[data-test=\"continue\"]").click()
#     page.locator("[data-test=\"finish\"]").click()
#     page.locator("[data-test=\"back-to-products\"]").click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)

# playwright codegen url
# playwright codegen https://www.saucedemo.com/

# import re
# from playwright.sync_api import Page, expect


# def test_example(page: Page) -> None:
#     page.goto("https://www.saucedemo.com/")
#     page.locator("[data-test=\"username\"]").click()
#     page.locator("[data-test=\"username\"]").fill("standard_user")
#     page.locator("[data-test=\"password\"]").click()
#     page.locator("[data-test=\"password\"]").fill("secret_sauce")
#     page.locator("[data-test=\"login-button\"]").click()
#     expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_be_visible()
#     expect(page.locator("[data-test=\"inventory-container\"]")).to_match_aria_snapshot("- link \"Sauce Labs Backpack\":\n  - /url: \"#\"\n  - img \"Sauce Labs Backpack\"\n- link \"Sauce Labs Backpack\":\n  - /url: \"#\"\n- text: /carry\\.allTheThings\\(\\) with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection\\. \\$\\d+\\.\\d+/\n- button \"Add to cart\"\n- link \"Sauce Labs Bike Light\":\n  - /url: \"#\"\n  - img \"Sauce Labs Bike Light\"\n- link \"Sauce Labs Bike Light\":\n  - /url: \"#\"\n- text: /A red light isn't the desired state in testing but it sure helps when riding your bike at night\\. Water-resistant with 3 lighting modes, 1 AAA battery included\\. \\$\\d+\\.\\d+/\n- button \"Add to cart\"\n- link \"Sauce Labs Bolt T-Shirt\":\n  - /url: \"#\"\n  - img \"Sauce Labs Bolt T-Shirt\"\n- link \"Sauce Labs Bolt T-Shirt\":\n  - /url: \"#\"\n- text: /Get your testing superhero on with the Sauce Labs bolt T-shirt\\. From American Apparel, \\d+% ringspun combed cotton, heather gray with red bolt\\. \\$\\d+\\.\\d+/\n- button \"Add to cart\"\n- link \"Sauce Labs Fleece Jacket\":\n  - /url: \"#\"\n  - img \"Sauce Labs Fleece Jacket\"\n- link \"Sauce Labs Fleece Jacket\":\n  - /url: \"#\"\n- text: /It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office\\. \\$\\d+\\.\\d+/\n- button \"Add to cart\"\n- link \"Sauce Labs Onesie\":\n  - /url: \"#\"\n  - img \"Sauce Labs Onesie\"\n- link \"Sauce Labs Onesie\":\n  - /url: \"#\"\n- text: /Rib snap infant onesie for the junior automation engineer in development\\. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel\\. \\$\\d+\\.\\d+/\n- button \"Add to cart\"\n- link \"Test.allTheThings() T-Shirt (Red)\":\n  - /url: \"#\"\n  - img \"Test.allTheThings() T-Shirt (Red)\"\n- link \"Test.allTheThings() T-Shirt (Red)\":\n  - /url: \"#\"\n- text: /This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests\\. Super-soft and comfy ringspun combed cotton\\. \\$\\d+\\.\\d+/\n- button \"Add to cart\"")
#     expect(page.locator("[data-test=\"secondary-header\"]")).to_match_aria_snapshot("- text: Products Name (A to Z)\n- combobox:\n  - option \"Name (A to Z)\" [selected]\n  - option \"Name (Z to A)\"\n  - option \"Price (low to high)\"\n  - option \"Price (high to low)\"")
import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.locator("body").click()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("sachin")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("sachinm")
    page.locator("[data-test=\"lastName\"]").fill("agar")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("200")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()
    page.locator("[data-test=\"back-to-products\"]").click()
    expect(page.locator("[data-test=\"primary-header\"]")).to_contain_text("Swag Labs")
