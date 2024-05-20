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


# Prueba de autenticación usando la fixture setup_teardown
def test_signup(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Sing up").click()
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("paco@gmail.com")
    page.get_by_label("Repeat password").click()
    page.get_by_label("Repeat password").fill("paco123")
    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="name@example.com").fill("paco123")
    page.get_by_role("button", name="Register").click()


def test_signup_with_account(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Sing up").click()
    page.get_by_role("link", name="Log in here").click()
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("admin")
    page.get_by_label("Password").press("Enter")


def test_login(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Log In").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("admin")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("admin")
    page.get_by_role("button", name="Log In").click()


def test_login_register(setup_teardown: Page):
    page = setup_teardown
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Log In").click()
    page.get_by_role("link", name="Register here").click()