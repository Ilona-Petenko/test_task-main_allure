import pytest
from framework import Logger
from tests.test_manager import handle_result, save_screenshot


@pytest.mark.parametrize(
    "email,password,result",
    [
        ("a", "qa_automation_password", False),
        ("qa.ajax.app.automation@gmail.com", "p", False),
        ("qa.ajax.app.automation@@gmail.com", "qa_automation_password", False),
        ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True),
    ]
)
def test_user_login(intro_page, login_page, device_list_page, email: str, password: str, result: bool, driver) -> None:
    intro_page.click_login_button()
    login_page.fill_email_data(email)
    login_page.fill_password_data(password)
    login_page.click_login_button()

    try:
        assert device_list_page.check_add_button_presents() == result
        Logger.logger.info(f"{'positive' if result else 'negative'} test passed with credentials. "
                           f"Email: {email} Password: {password}")
    except AssertionError:
        Logger.logger.error(f"Test failed with {'valid' if result else 'not valid'} credentials. "
                            f"Email: {email} Password: {password}")
        raise
    finally:
        if not result:
            login_page.go_back()
