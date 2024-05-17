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
        page.get_by_label("Contraseña").click()
        page.get_by_label("Contraseña").fill("admin")
        page.get_by_label("Contraseña").press("Enter")
        page.get_by_role("link", name="Movies").click()

        yield page
        context.close()
        browser.close()


def movie_test_1(setup_teardown: Page):
    page = setup_teardown
    expect(page.get_by_role("list")).to_contain_text("Home")
    expect(page.get_by_role("list")).to_contain_text("Movies")
    expect(page.get_by_role("list")).to_contain_text("Series")
    expect(page.get_by_role("list")).to_contain_text("Log In")
    expect(page.get_by_role("list")).to_contain_text("Sing up")
    expect(page.locator("h1")).to_contain_text("Popular movies")
    page.get_by_placeholder("Movie title...").click()
    page.get_by_placeholder("Movie title...").fill("sherlock holmes")
    page.get_by_placeholder("Movie title...").press("Enter")
    expect(page.locator("#search-results")).to_contain_text(
        "Eccentric consulting detective Sherlock Holmes and Doctor John Watson battle to bring down a new nemesis and unravel a deadly plot that could destroy England.")
    expect(page.locator("#search-results")).to_contain_text("Sherlock Holmes")
    expect(page.get_by_text(
        "Sherlock Holmes Eccentric consulting detective Sherlock Holmes and Doctor John Watson battle to bring down a new nemesis and unravel a deadly plot that could destroy England. Fecha de lanzamiento: 2009-12-23 Puntuación media:")).to_be_visible()
    page.get_by_text(
        "Sherlock Holmes Eccentric consulting detective Sherlock Holmes and Doctor John Watson battle to bring down a new nemesis and unravel a deadly plot that could destroy England. Fecha de lanzamiento: 2009-12-23 Puntuación media:").click()
    expect(page.get_by_role("heading")).to_contain_text("Sherlock Holmes")
    expect(page.get_by_role("img", name="Sherlock Holmes")).to_be_visible()
    expect(page.get_by_role("paragraph")).to_contain_text(
        "Eccentric consulting detective Sherlock Holmes and Doctor John Watson battle to bring down a new nemesis and unravel a deadly plot that could destroy England.")


def movie_test_2(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Movies").click()
    expect(page.get_by_role("list")).to_contain_text("Home")
    expect(page.get_by_role("list")).to_contain_text("Movies")
    expect(page.get_by_role("list")).to_contain_text("Series")
    expect(page.get_by_role("list")).to_contain_text("Log In")
    expect(page.get_by_role("list")).to_contain_text("Sing up")
    expect(page.locator("h1")).to_contain_text("Popular movies")
    page.get_by_placeholder("Movie title...").click()
    page.get_by_placeholder("Movie title...").fill("el padrino")
    page.get_by_placeholder("Movie title...").press("Enter")
    expect(page.locator("#search-results")).to_contain_text(
        "In the streets of East Los Angeles, Manny is a formidable drug dealer. Impressed by his extravagant lifestyle and prowess, his young son, Kilo, yearns to follow in his footsteps. Kilo resolves to learn how to prosper in the drug world, and his new life as a dealer begins. In a world where a man wants everything, he may end up with nothing.")
    expect(page.locator("#search-results")).to_contain_text("El padrino: The Latin Godfather")
    page.get_by_text(
        "El padrino: The Latin Godfather In the streets of East Los Angeles, Manny is a formidable drug dealer. Impressed by his extravagant lifestyle and prowess, his young son, Kilo, yearns to follow in his footsteps. Kilo resolves to learn how to prosper in the drug world, and his new life as a dealer begins. In a world where a man wants everything, he may end up with nothing. Fecha de lanzamiento: 2004-09-27 Puntuación media:").click()
    expect(page.get_by_role("heading")).to_contain_text("El padrino: The Latin Godfather")
    expect(page.get_by_role("paragraph")).to_contain_text(
        "In the streets of East Los Angeles, Manny is a formidable drug dealer. Impressed by his extravagant lifestyle and prowess, his young son, Kilo, yearns to follow in his footsteps. Kilo resolves to learn how to prosper in the drug world, and his new life as a dealer begins. In a world where a man wants everything, he may end up with nothing.")
    expect(page.get_by_role("img", name="El padrino: The Latin")).to_be_visible()
    expect(page.get_by_role("rowgroup")).to_contain_text("Presupuesto")
