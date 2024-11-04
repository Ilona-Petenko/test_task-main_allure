from .page import Page


class IntroPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_button = "com.ajaxsystems:id/authHelloLogin"

    def click_login_button(self):
        self.find_element_by_id(self.login_button).click()

