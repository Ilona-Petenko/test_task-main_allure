from application.pages.page import Page


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_button = "com.ajaxsystems:id/authLogin"
        self.email_data = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText"
        self.password_data = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[2]/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText"

    def fill_email_data(self, email: str):
        email_field = self.find_element_by_xpath(self.email_data)
        email_field.click()
        email_field = self.find_element_by_xpath(self.email_data)
        email_field.send_keys(email)

    def fill_password_data(self, password: str):
        password_field = self.find_element_by_xpath(self.password_data)
        password_field.click()
        password_field = self.find_element_by_xpath(self.password_data)
        password_field.send_keys(password)

    def go_back(self):
        back_button = self.find_element_by_id('com.ajaxsystems:id/back')
        back_button.click()

    def click_login_button(self):
        self.find_element_by_id(self.login_button).click()

    def clear_email(self):
        email_field = self.find_element_by_xpath(self.email_data)
        email_field.clear()
