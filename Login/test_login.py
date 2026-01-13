import re

from playwright.sync_api import Page, expect

def test_login(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")

    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()

    expect(page).to_have_title("Swag Labs")
    #click add to cart button. As ther are many add to cart button it click s the first add to click button 
    page.get_by_role("button", name="Add to cart").first.click()