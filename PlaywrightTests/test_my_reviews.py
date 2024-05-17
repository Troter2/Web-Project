import pytest
import time
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


def test_my_reviews_buttons(setup_teardown: Page):
    page = setup_teardown
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Log In").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("admin")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("admin")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("link", name="Movies").click()
    page.get_by_text("Kingdom of the Planet of the Apes Several generations in the future following Caesar's reign, apes are now the dominant species and live harmoniously while humans have been reduced to living in the shadows. As a new tyrannical ape le… Release date: 2024-05-08 Average rating:").click()
    time.sleep(1)
    page.get_by_role("button", name="Comment").click()
    page.get_by_placeholder("Leave a comment here").click()
    page.get_by_placeholder("Leave a comment here").fill("really bad.")
    page.get_by_role("button", name="Publish").click()
    page.get_by_role("button", name="admin").click()
    page.get_by_role("link", name="My Reviews").click()
    time.sleep(1)
    page.get_by_role("row", name="Kingdom of the Planet of the").locator("#view").click()
    page.get_by_role("button", name="Close").click()
    time.sleep(1)
    page.get_by_role("row", name="Kingdom of the Planet of the").locator("#edit").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("Worst movie ever.")
    page.get_by_role("button", name="Save Changes").click()
    time.sleep(1)
    page.get_by_role("row", name="Kingdom of the Planet of the").locator("#delete").click()
    page.get_by_role("button", name="Delete").click()
