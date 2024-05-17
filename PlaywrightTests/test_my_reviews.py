import pytest
from playwright.sync_api import sync_playwright, Page, expect


# Fixture de pytest para inicializar y cerrar el navegador antes y después de cada prueba
@pytest.fixture(scope="function")
def setup_teardown():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://localhost:8000/")
        yield page
        context.close()
        browser.close()


def test_my_reviews_button1(setup_teardown: Page):
    page = setup_teardown
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Log In").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("admin")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("admin")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("button", name="admin").click()
    page.get_by_role("link", name="My Reviews").click()
    page.get_by_role("row", name="Ley y orden: Unidad de Ví").get_by_role("button").first.click()
    page.get_by_role("button", name="Close").click()


def test_my_reviews_button2(setup_teardown: Page):
    page = setup_teardown
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Log In").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("admin")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("admin")
    page.get_by_label("Password").press("Enter")
    page.get_by_role("button", name="admin").click()
    page.get_by_role("link", name="My Reviews").click()
    page.get_by_role("row", name="Ley y orden: Unidad de Ví").get_by_role("button").nth(1).click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("Good Serie. Good trama.")
    page.locator("#rateYoM10 > .jq-ry-group-wrapper > .jq-ry-rated-group > svg:nth-child(5) > polygon").first.click()
    page.get_by_role("button", name="Save Changes").click()
