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
    expect(page.get_by_role("img", name="login form")).to_be_visible()
    expect(page.locator("span")).to_contain_text("Sign up")
    expect(page.get_by_role("paragraph")).to_contain_text("Already have an account? Log in here")
    page.get_by_placeholder("Username").fill("manolo")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("manolo@alumnes.udl.cat")
    page.get_by_label("Pasword").click()
    page.get_by_label("Pasword").fill("manolo123")
    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="name@example.com").fill("manolo123")
    page.get_by_role("button", name="Register").click()


def test_signup_with_account(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Sing up").click()
    expect(page.get_by_role("img", name="login form")).to_be_visible()
    expect(page.locator("span")).to_contain_text("Sign up")
    expect(page.locator("form")).to_contain_text("Register")
    expect(page.locator("form")).to_contain_text("Password requirements")
    page.get_by_label("Usuario").click()
    page.get_by_label("Usuario").fill("aurelio")
    page.get_by_label("Contraseña").click()
    page.get_by_label("Contraseña").fill("aurelio")
    page.get_by_label("Contraseña").press("Enter")
    page.get_by_label("Contraseña").click()
    page.get_by_label("Contraseña").click()
    page.get_by_label("Contraseña").fill("aurelio123")
    expect(page.get_by_role("img", name="login form")).to_be_visible()
    expect(page.locator("span")).to_contain_text("Sign in")
    page.get_by_role("button", name="Login").click()


def login_test(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Log In").click()
    expect(page.get_by_role("img", name="login form")).to_be_visible()
    expect(page.locator("span")).to_contain_text("Sign in")
    page.get_by_label("Usuario").click()
    page.get_by_label("Usuario").fill("aurelio")
    page.get_by_label("Contraseña").click()
    page.get_by_label("Contraseña").fill("aurelio123")
    page.get_by_role("button", name="Login").click()


def login_test_register(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Log In").click()
    expect(page.locator("span")).to_contain_text("Sign in")
    expect(page.get_by_role("img", name="login form")).to_be_visible()
    expect(page.get_by_role("paragraph")).to_contain_text("Don't have an account? Register here")
    page.get_by_role("link", name="Register here").click()