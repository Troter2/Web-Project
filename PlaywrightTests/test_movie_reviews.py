import pytest
import time
from playwright.sync_api import sync_playwright, Page, expect


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


def test_movie_review_no_login(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Movies").click()
    page.get_by_placeholder("Movie title...").click()
    page.get_by_placeholder("Movie title...").fill("dune")
    page.get_by_placeholder("Movie title...").press("Enter")
    page.get_by_text("Paul Atreides, a brilliant").click()
    page.get_by_text("Dune Paul Atreides, a").click()


def test_movie_review_login(setup_teardown: Page):
    page = setup_teardown
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Log In").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("admin")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("admin")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("link", name="Movies").click()
    page.get_by_placeholder("Movie title...").click()
    page.get_by_placeholder("Movie title...").fill("dune")
    page.locator("#button-addon2").click()
    page.get_by_text(
        "Dune Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding, must travel to the most dangerous planet in the universe to ensure the future of his family and his people. As malevolent forces explode into conflict over the planet's exclusive supply of the most precious resource in existence-a commodity capable of unlocking humanity's greatest potential-only those who can conquer their fear will survive. Release date: 2021-09-15 Average rating:").click()

    time.sleep(1)
    page.locator("#comment_buttom").click()
    page.get_by_placeholder("Leave a comment here").click()
    page.get_by_placeholder("Leave a comment here").fill("mala")
    page.get_by_role("button", name="Publish").click()
    time.sleep(1)
    page.locator("#comment_buttom").click()
    page.get_by_placeholder("Leave a comment here").fill("bona")
    time.sleep(1)
    page.get_by_role("button", name="Publish").click()


