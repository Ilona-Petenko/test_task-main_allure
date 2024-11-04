import pytest

from framework import Logger

Logger.logger.debug("test starts")


@pytest.mark.parametrize(
    "id_element",
    [
        'com.ajaxsystems:id/settings',
        'com.ajaxsystems:id/help',
        'com.ajaxsystems:id/logs',
        'com.ajaxsystems:id/camera'
    ]
)
def test_sidebar(intro_page, login_page, device_list_page, sidebar_page, app_setting_page, id_element: str) -> None:
    Logger.logger.warning('WARNING')
    intro_page.click_login_button()
    login_page.clear_email()
    login_page.fill_email_data('qa.ajax.app.automation@gmail.com')
    login_page.fill_password_data('qa_automation_password')
    login_page.click_login_button()
    device_list_page.click_side_bar()
    try:
        assert sidebar_page.find_element_by_id(id_element)
        if True:
            assert sidebar_page.find_element_by_id(id_element)
            sidebar_page.click_app_setting()
            app_setting_page.click_sign_out()
    except AssertionError:
        Logger.logger.error(f"{id_element} isn't found")
        assert sidebar_page.find_element_by_id(id_element)
    else:
        Logger.logger.info(f"{id_element} is found")
