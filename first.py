from playwright.sync_api import sync_playwright
# Start Playwright engine
with sync_playwright() as p:
 # Launch browser (Chromium)
    browser = p.chromium.launch(headless=False)
 # Open a new browser page
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    print(page.title())

    #close browser
    browser.close()

 # Navigate to the website
#  page.goto("https://www.saucedemo.com/")
#  # Click link using text locator
#  page.get_by_placeholder("Username").fill("standard_user")
#     #send password
#  page.get_by_placeholder("Password").fill("secret_sauce")
#  page.get_by_role("button", name="Login").click()


 # Close the browser
    