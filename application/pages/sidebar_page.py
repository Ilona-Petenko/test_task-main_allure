from .page import Page


class Sidebar(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def click_app_setting(self):
        self.find_element_by_id('com.ajaxsystems:id/settings').click()
