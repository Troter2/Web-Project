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


def test_serie_review_no_login(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Series").click()
    page.get_by_placeholder("Serie title...").click()
    page.get_by_placeholder("Serie title...").fill("bones")
    page.get_by_placeholder("Serie title...").press("Enter")
    page.get_by_text("Dr. Temperance Brennan and").click()
    page.get_by_text("Bones Una antropóloga forense").click()
    page.get_by_text("Bones Una antropóloga forense").click()
    page.get_by_text("Bones Una antropóloga forense").click()
    expect(page.get_by_role("img", name="Bones")).to_be_visible()
    expect(page.get_by_role("heading")).to_contain_text("Bones")



def test_serie_review_login(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Login In").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("admin")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("admin")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("link", name="Series").click()
    page.get_by_placeholder("Serie title...").click()
    page.get_by_placeholder("Serie title...").click()
    page.get_by_placeholder("Serie title...").fill("bones")
    page.get_by_placeholder("Serie title...").press("Enter")
    page.get_by_text("Bones Dr. Temperance Brennan and her colleagues at the Jeffersonian's Medico-Legal Lab assist Special Agent Seeley Booth with murder investigations when the remains are so badly decomposed, burned or destroyed that the standard identification methods are useless. Release Date: 2005-09-13 Average Rating:").click()
    page.get_by_role("button", name="Comment").click()
    page.get_by_placeholder("Leave a comment here").click()
    page.get_by_placeholder("Leave a comment here").fill("")
    page.get_by_role("button", name="Publish").click()
    page.get_by_placeholder("Leave a comment here").click()
    page.get_by_placeholder("Leave a comment here").fill("Bona Peli pero hi han aspectes a millorar")
    page.locator(".jq-ry-rated-group > svg:nth-child(2) > polygon").click()
    page.locator(".jq-ry-rated-group > svg > polygon").first.click()
    page.get_by_text("Review Publish").click()
    page.get_by_role("button", name="Publish").click()
    page.get_by_placeholder("Leave a comment here").fill("Malisima")
    page.get_by_role("button", name="Publish").click()
    page.get_by_placeholder("Leave a comment here").fill("La millor peli que he vist en molt temps")
    page.locator(".jq-ry-rated-group > svg:nth-child(5) > polygon").click()
    page.get_by_role("button", name="Publish").click()