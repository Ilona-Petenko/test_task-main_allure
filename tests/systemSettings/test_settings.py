import pytest

from framework import Logger

Logger.logger.debug("test starts")


def test_background_connection(login_to_acc, device_list_page, sidebar_page, app_setting_page, system_setting_page):
    Logger.logger.warning('WARNING')
    device_list_page.click_side_bar()
    sidebar_page.click_app_setting()
    app_setting_page.click_system_setting()
    try:
        assert (system_setting_page.check_background_connection_section()
                and system_setting_page.check_background_connection_title()
                and system_setting_page.check_toggle_on_background_connection())
    except AssertionError:
        Logger.logger.error("Element isn't found")
    else:
        Logger.logger.info("Element is found")
    system_setting_page.click_toggle_on_background_connection()
    system_setting_page.click_back_button()
    app_setting_page.click_system_setting()
    assert system_setting_page.check_toggle_off_background_connection()
    system_setting_page.click_toggle_off_background_connection()
    system_setting_page.click_back_button()
    app_setting_page.click_system_setting()
    assert system_setting_page.check_toggle_on_background_connection()


def test_keep_alive(login_to_acc, device_list_page, sidebar_page, app_setting_page, system_setting_page):
    Logger.logger.warning('WARNING')
    device_list_page.click_side_bar()
    sidebar_page.click_app_setting()
    app_setting_page.click_system_setting()
    try:
        assert (system_setting_page.check_keep_alive_section()
            and system_setting_page.check_keep_alive_descr()
            and system_setting_page.check_toggle_on_keep_alive())
    except AssertionError:
        Logger.logger.error("Element isn't found")
    else:
        Logger.logger.info("Element is found")
    system_setting_page.click_toggle_on_keep_alive()
    system_setting_page.click_back_button()
    app_setting_page.click_system_setting()
    assert system_setting_page.check_toggle_off_keep_alive()
    system_setting_page.click_toggle_off_keep_alive()
    system_setting_page.click_back_button()
    app_setting_page.click_system_setting()
    assert system_setting_page.check_toggle_on_keep_alive()


def test_units_measurement(login_to_acc, device_list_page, sidebar_page, app_setting_page, system_setting_page):
    Logger.logger.warning('WARNING')
    device_list_page.click_side_bar()
    sidebar_page.click_app_setting()
    app_setting_page.click_system_setting()
    try:
        assert (system_setting_page.check_units_measurement_section()
                and system_setting_page.check_units_measurement_descr()
                and system_setting_page.check_units_measurement_dropdown())
    except AssertionError:
        Logger.logger.error("Element isn't found")
    else:
        Logger.logger.info("Element is found")
    system_setting_page.click_units_measurement_dropdown()
    system_setting_page.click_dropdown_imperial()
    assert system_setting_page.dropdown_imperial()
    system_setting_page.click_units_measurement_dropdown()
    system_setting_page.click_dropdown_metric()
    assert system_setting_page.dropdown_metric()
