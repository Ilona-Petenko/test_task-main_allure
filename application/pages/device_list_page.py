from .page import Page


class DeviceListPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

        self.add_button = "com.ajaxsystems:id/hubAdd"
        self.side_bar = "com.ajaxsystems:id/menuDrawer"

    def check_add_button_presents(self) -> bool:
        try:
            self.find_element_by_id(self.add_button)
            return True
        except Exception:
            return False

    def click_side_bar(self):
        self.find_element_by_id(self.side_bar).click()
