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
        page.get_by_role("link", name="Log In").click()
        page.get_by_label("Username").click()
        page.get_by_label("Username").fill("admin")
        page.get_by_label("Password").click()
        page.get_by_label("Password").fill("admin")
        page.get_by_role("button", name="Log In").click()
        yield page
        context.close()
        browser.close()


def test_serie_1(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Series").click()
    page.get_by_placeholder("Serie title...").click()
    page.get_by_placeholder("Serie title...").fill("bones")
    page.locator("#button-addon2").click()
    page.get_by_text(
        "Bones Dr. Temperance Brennan and her colleagues at the Jeffersonian's Medico-Legal Lab assist Special Agent Seeley Booth with murder investigations when the remains are so badly decomposed, burned or destroyed that the standard identification methods are useless. Release Date: 2005-09-13 Average Rating:").click()
    expect(page.get_by_role("main")).to_contain_text(
        "Una antropóloga forense y un engreído agente del FBI forman equipo para investigar las causas de los homicidios que investigan.")


def test_serie_2(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Series").click()
    page.get_by_placeholder("Serie title...").click()
    page.get_by_placeholder("Serie title...").fill("falcon Crest")
    page.locator("#button-addon2").click()
    page.get_by_role("heading", name="Falcon Crest").click()
