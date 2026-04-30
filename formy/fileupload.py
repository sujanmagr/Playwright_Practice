from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)

    page=browser.new_page()

    page.goto("https://formy-project.herokuapp.com/fileupload")


    page.locator("#file-upload-field").set_input_files('all.py')
    browser.close()





