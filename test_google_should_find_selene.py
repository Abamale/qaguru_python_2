import pytest
from selene import be, have
from selene.support.shared import browser


@pytest.fixture
def configured_browser():
    browser.config.window_height = 980
    browser.config.window_width = 670
    return browser


@pytest.fixture
def define_url():
    browser.open('https://google.com')


def test_google_research(configured_browser, define_url):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_for_conflict():
    assert 3 > 1
