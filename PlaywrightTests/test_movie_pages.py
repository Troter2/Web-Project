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
        page.get_by_label("Password").fill("admin")
        page.get_by_label("Password").press("Enter")
        page.get_by_role("link", name="Movies").click()

        yield page
        context.close()
        browser.close()


def test_movie_1(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Movies").click()
    page.get_by_placeholder("Movie title...").click()
    page.get_by_placeholder("Movie title...").fill("godzilla")
    page.get_by_placeholder("Movie title...").press("Enter")
    page.get_by_text(
        "Godzilla Ford Brody, a Navy bomb expert, has just reunited with his family in San Francisco when he is forced to go to Japan to help his estranged father, Joe. Soon, both men are swept up in an escalating crisis when an ancient alpha predator arises from the sea to combat malevolent adversaries that threaten the survival of humanity. The creatures leave colossal destruction in their wake, as they make their way toward their final battleground: San Francisco. Release date: 2014-05-14 Average rating:").click()
    expect(page.get_by_role("paragraph")).to_contain_text(
        "Ford Brody, a Navy bomb expert, has just reunited with his family in San Francisco when he is forced to go to Japan to help his estranged father, Joe. Soon, both men are swept up in an escalating crisis when an ancient alpha predator arises from the sea to combat malevolent adversaries that threaten the survival of humanity. The creatures leave colossal destruction in their wake, as they make their way toward their final battleground: San Francisco.")


def test_movie_2(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Movies").click()
    page.get_by_placeholder("Movie title...").click()
    page.get_by_placeholder("Movie title...").fill("sherlock")
    page.locator("#button-addon2").click()
    page.get_by_text(
        "Sherlock Holmes Eccentric consulting detective Sherlock Holmes and Doctor John Watson battle to bring down a new nemesis and unravel a deadly plot that could destroy England. Release date: 2009-12-23 Average rating:").click()
    expect(page.get_by_role("main")).to_contain_text(
        "Eccentric consulting detective Sherlock Holmes and Doctor John Watson battle to bring down a new nemesis and unravel a deadly plot that could destroy England.")

