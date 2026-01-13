import re
from playwright.sync_api import Page, expect


def test_login(page: Page):
    #goto the login page
    page.goto("https://www.saucedemo.com/")
    #send username
    page.get_by_placeholder("Username").fill("standard_user")
    #send password

    page.get_by_placeholder("Password").fill("secret_sauce")


    #click login button
    page.get_by_role("button", name="Login").click()

    #check if login is successful and the changed url 
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    print("login successful")

# To run this pytest --headed --slowmo=500