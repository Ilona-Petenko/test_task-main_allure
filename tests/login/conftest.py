import pytest
from application.pages import DeviceListPage, IntroPage, LoginPage
from tests.conftest import driver


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def intro_page(driver):
    return IntroPage(driver)


@pytest.fixture
def device_list_page(driver):
    return DeviceListPage(driver)
