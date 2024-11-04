from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element_by_xpath(self, xpath: str) -> WebElement:
        wait = WebDriverWait(self.driver, 20)
        return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def find_element_by_id(self, id_: str) -> WebElement:
        wait = WebDriverWait(self.driver, 20)
        return wait.until(EC.presence_of_element_located((By.ID, id_)))

    def click_element(self):
        raise NotImplementedError
