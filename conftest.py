import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser(pytestconfig):
    return pytestconfig.getoption("browser")[0]


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("base_url")


@pytest.fixture(scope="function")
def driver(base_url: str, browser: str):
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, browser)
        browser = browser_type.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(base_url, timeout=50000)

        yield page

        page.close()
        context.close()
        browser.close()
