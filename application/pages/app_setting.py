from .page import Page


class AppSetting(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def click_system_setting(self):
        self.find_element_by_id("com.ajaxsystems:id/accountInfoSettingsNavigate").click()

    def click_sign_out(self):
        self.find_element_by_id("com.ajaxsystems:id/accountInfoLogoutNavigate").click()
