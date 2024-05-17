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
        page.get_by_label("Usuario").click()
        page.get_by_label("Usuario").fill("admin")
        page.get_by_label("Contraseña").click()
        page.get_by_label("Contraseña").fill("admin")
        page.get_by_role("button", name="Login").click()
        yield page
        context.close()
        browser.close()


def serie_test(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Series").click()
    expect(page.locator("h1")).to_contain_text("Popular series")
    page.get_by_placeholder("Serie title...").click()
    page.get_by_placeholder("Serie title...").click()
    page.get_by_placeholder("Serie title...").fill("bones")
    page.get_by_placeholder("Serie title...").press("Enter")
    page.get_by_text(
        "Bones Dr. Temperance Brennan and her colleagues at the Jeffersonian's Medico-Legal Lab assist Special Agent Seeley Booth with murder investigations when the remains are so badly decomposed, burned or destroyed that the standard identification methods are useless. Fecha de lanzamiento: 2005-09-13 Puntuación media:").click()
    expect(page.get_by_role("img", name="Bones")).to_be_visible()
    expect(page.get_by_role("heading")).to_contain_text("Bones")
    expect(page.get_by_role("paragraph")).to_contain_text(
        "Una antropóloga forense y un engreído agente del FBI forman equipo para investigar las causas de los homicidios que investigan.")
    expect(page.get_by_role("rowgroup")).to_contain_text("Numero de temporadas")


def serie2_test(setup_teardown: Page):
    page = setup_teardown
    page.get_by_role("link", name="Series").click()
    expect(page.locator("h1")).to_contain_text("Popular series")
    expect(page.get_by_role("list")).to_contain_text("Log In")
    expect(page.get_by_role("list")).to_contain_text("Sing up")
    expect(page.get_by_role("list")).to_contain_text("Home")
    expect(page.get_by_role("list")).to_contain_text("Movies")
    page.get_by_placeholder("Serie title...").click()
    page.get_by_placeholder("Serie title...").fill("Falcon Crest")
    page.get_by_placeholder("Serie title...").press("Enter")
    page.get_by_text("Falcon Crest Falcon Crest is").click()
    expect(page.get_by_role("paragraph")).to_contain_text(
        "Serie de TV (1981-1990). 9 temporadas. 227 episodios. En el valle de Tuscany, una fértil región que produce los mejores vinos de California, la acaudalda familia Channing intenta mantener su poder y hacer prosperar sus negocios vinícolas. Encabezados por la implacable matriarca Angela Channing, casi todos los miembros de la familia llevan una azarosa vida de amplia repercusión en toda la región, un modo de vivir donde el lujo, el poder, las traiciones, engaños, romances y luchas sin cuartel están a la orden del día. Angela Channing ha heredado los viñedos de Falcon Crest, que su abuelo italiano levantó con tanto éxito. Cuando Jason Gioberti, el hermano de Ángela, muere accidentalmente por culpa de su hija Emma, 50 acres del productivo viñedo pasan a ser propiedad de su hijo Chase. Angela está convencida de que esa tierra le pertenece. Los problemas surgen cuando, inesperadamente, Chase, que vive en Nueva York, se muda a Tuscany con su encantadora mujer Maggie y sus dos hijos, Cole y Victoria, con la intención de ocuparse de las tierras que acaba de heredar.")
    expect(page.get_by_role("heading")).to_contain_text("Falcon Crest")
