from .page import Page


class SystemSetting(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.toggle_background_connection = '//android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView[1]/android.view.View[1]/android.view.View/android.view.View'
        self.back_button = '//android.view.View/android.view.View/android.widget.ScrollView[2]/android.widget.ImageView'
        self.background_connection_title = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView[1]/android.widget.TextView[1]'
        self.background_connection_section = 'com.ajaxsystems:id/appSettingsBackgroundConnection'
        self.keep_alive_section = 'com.ajaxsystems:id/appSettingsKeepAlive'
        self.keep_alive_descr = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView[1]/android.widget.TextView[3]'
        self.toggle_keep_alive = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView[1]/android.view.View[3]/android.view.View/android.view.View'
        self.units_measurement_section = 'com.ajaxsystems:id/appSettingsMeasurementSystem'
        self.units_measurement_title = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView[1]/android.widget.TextView[5]'
        self.units_measurement_descr = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView[1]/android.widget.TextView[6]'
        self.units_measurement_dropdown = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView[1]/android.view.View[5]/android.view.View[2]/android.view.View'
        self.automatically = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]'
        self.metric = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]'
        self.imperial = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.TextView'

    def click_back_button(self):
        self.find_element_by_xpath(self.back_button).click()

    def check_background_connection_section(self) -> bool:
        try:
            self.find_element_by_id(self.background_connection_section)
            return True
        except AssertionError:
            return False

    def check_background_connection_title(self) -> bool:
        try:
            self.find_element_by_xpath(self.background_connection_title)
            return True

        except AssertionError:
            return False

    def click_toggle_on_background_connection(self):
        try:
            toggle_on = self.find_element_by_xpath(self.toggle_background_connection).get_attribute("checked") == "true"
            self.find_element_by_xpath(self.toggle_background_connection).click()
            return toggle_on
        except AssertionError:
            return False

    def check_toggle_on_background_connection(self):
        try:
            toggle_on = self.find_element_by_xpath(self.toggle_background_connection).get_attribute("checked") == "true"
            return toggle_on
        except AssertionError:
            return False

    def click_toggle_off_background_connection(self):
        try:
            toggle_off = self.find_element_by_xpath(self.toggle_background_connection).get_attribute(
                "checked") == "false"
            self.find_element_by_xpath(self.toggle_background_connection).click()
            return toggle_off
        except AssertionError:
            return False

    def check_toggle_off_background_connection(self):
        try:
            toggle_off = self.find_element_by_xpath(self.toggle_background_connection).get_attribute(
                "checked") == "false"
            return toggle_off
        except AssertionError:
            return False

    def check_keep_alive_section(self) -> bool:
        try:
            self.find_element_by_id(self.keep_alive_section)
            return True
        except AssertionError:
            return False

    def check_keep_alive_descr(self) -> bool:
        try:
            self.find_element_by_xpath(self.keep_alive_descr)
            return True
        except AssertionError:
            return False

    def click_toggle_on_keep_alive(self):
        try:
            toggle_on = self.find_element_by_xpath(self.toggle_keep_alive).get_attribute("checked") == "true"
            self.find_element_by_xpath(self.toggle_keep_alive).click()
            return toggle_on
        except AssertionError:
            return False

    def check_toggle_on_keep_alive(self):
        try:
            toggle_on = self.find_element_by_xpath(self.toggle_keep_alive).get_attribute("checked") == "true"
            return toggle_on
        except AssertionError:
            return False

    def click_toggle_off_keep_alive(self):
        try:
            toggle_off = self.find_element_by_xpath(self.toggle_keep_alive).get_attribute("checked") == "false"
            self.find_element_by_xpath(self.toggle_keep_alive).click()
            return toggle_off
        except AssertionError:
            return False

    def check_toggle_off_keep_alive(self):
        try:
            toggle_off = self.find_element_by_xpath(self.toggle_keep_alive).get_attribute("checked") == "false"
            return toggle_off
        except AssertionError:
            return False

    def check_units_measurement_section(self) -> bool:
        try:
            self.find_element_by_id(self.units_measurement_section)
            return True
        except AssertionError:
            return False

    def check_units_measurement_descr(self) -> bool:
        try:
            self.find_element_by_xpath(self.units_measurement_descr)
            return True
        except AssertionError:
            return False

    def check_units_measurement_dropdown(self) -> bool:
        try:
            self.find_element_by_xpath(self.units_measurement_dropdown)
            return True
        except AssertionError:
            return False

    def click_units_measurement_dropdown(self):
        self.find_element_by_xpath(self.units_measurement_dropdown).click()

    def tap_screen_outside(self):
        self.find_element_by_id('com.ajaxsystems:id/touch_outside').click()

    def dropdown_automatically(self):
        self.find_element_by_xpath(self.automatically).click()


    def  dropdown_metric(self):
        try:
            self.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView[1]/android.view.View[5]/android.view.View[1]")
            return True
        except AssertionError:
            return False

    def click_dropdown_metric(self):
        self.find_element_by_xpath(self.metric).click()

    def dropdown_imperial(self):
        try:
            self.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView[1]/android.view.View[5]/android.view.View[1]")
            return True
        except AssertionError:
            return False

    def click_dropdown_imperial(self):
        self.find_element_by_xpath(self.imperial).click()

