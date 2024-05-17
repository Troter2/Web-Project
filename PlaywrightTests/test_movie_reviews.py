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
    page.get_by_placeholder("Movie title...").fill("origen")
    page.get_by_placeholder("Movie title...").press("Enter")
    page.get_by_text("Origen Fecha de lanzamiento: 2020-07-30 Puntuación media:").click()
    page.get_by_text("Origen Fecha de lanzamiento").click()
    page.get_by_text("Origen Fecha de lanzamiento").click()
    expect(page.get_by_role("heading")).to_contain_text("Origen")
    expect(page.get_by_role("img", name="Origen")).to_be_visible()


def test_movie_review_login(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Log In").click()
    page.get_by_label("Usuario").click()
    page.get_by_label("Usuario").fill("admin")
    page.get_by_label("Contraseña").click()
    page.get_by_label("Contraseña").fill("admin")
    page.get_by_label("Contraseña").press("Enter")
    page.get_by_role("button", name="admin").click()
    page.get_by_role("link", name="Movies").click()
    page.get_by_placeholder("Movie title...").click()
    page.get_by_placeholder("Movie title...").fill("dune")
    page.get_by_placeholder("Movie title...").press("Enter")
    page.get_by_text(
        "Dune Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding, must travel to the most dangerous planet in the universe to ensure the future of his family and his people. As malevolent forces explode into conflict over the planet's exclusive supply of the most precious resource in existence-a commodity capable of unlocking humanity's greatest potential-only those who can conquer their fear will survive. Fecha de lanzamiento: 2021-09-15 Puntuación media:").click()
    page.get_by_role("button", name="Comentar").click()
    page.get_by_placeholder("Leave a comment here").click()
    page.get_by_placeholder("Leave a comment here").fill("Bastant sobrevalorada la peli la verda")
    page.locator(".jq-ry-rated-group > svg > polygon").first.click()
    page.get_by_role("button", name="Publicar").click()
    page.get_by_text("Dune Paul Atreides, a").click()
    page.get_by_placeholder("Leave a comment here").fill("la peli es molt bona")
    page.locator(".jq-ry-rated-group > svg:nth-child(5) > polygon").click()
    page.get_by_role("button", name="Publicar").click()
    page.get_by_placeholder("Leave a comment here").fill("es pot millorar molta cosa encara")
    page.get_by_role("button", name="Publicar").click()

