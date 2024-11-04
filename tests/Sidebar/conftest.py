import pytest
from application.pages import DeviceListPage, IntroPage, LoginPage, Sidebar, AppSetting
from application.pages.page import Page
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


@pytest.fixture
def sidebar_page(driver):
    return Sidebar(driver)


@pytest.fixture
def app_setting_page(driver):
    return AppSetting(driver)
