import pytest
import allure
from _pytest.reports import TestReport
from _pytest.runner import call_runtest_hook, check_interactive_exception
from allure_commons.types import AttachmentType


def save_xml(driver) -> None:
    xml = driver.page_source
    filename = "page_source.xml"
    with open(filename, 'w') as file:
        file.write(xml)
    allure.attach(xml, name=filename, attachment_type=AttachmentType.XML)

def save_screenshot(driver) -> None:
    full_screenshot_data = driver.get_screenshot_as_png()
    allure.attach(full_screenshot_data, name="Screenshot", attachment_type=AttachmentType.PNG)

def handle_result(driver) -> None:
    save_xml(driver)
    save_screenshot(driver)