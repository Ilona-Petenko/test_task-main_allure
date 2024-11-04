import pytest
from application.pages import DeviceListPage, IntroPage, LoginPage, Sidebar, AppSetting, SystemSetting
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

@pytest.fixture
def system_setting_page(driver):
    return SystemSetting(driver)

@pytest.fixture
def login_to_acc(intro_page, login_page, sidebar_page, app_setting_page, device_list_page):
    intro_page.click_login_button()
    login_page.fill_email_data('qa.ajax.app.automation@gmail.com')
    login_page.fill_password_data('qa_automation_password')
    login_page.click_login_button()
    return DeviceListPage(driver)