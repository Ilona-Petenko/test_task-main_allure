
from typing import Optional

import allure
import pytest
from allure_commons.types import AttachmentType
from framework import Logger


def save_xml(cls, log: str) -> None:
    xml = cls.page_source()
    xmls = cls.get_file(xml, log)

    for filename, data in xmls:
        cls.save_file(data, cls.get_folder(), filename + '.xml', AttachmentType.XML, 'w')


def save_screenshot(cls, log: str, additional_screenshot_data: Optional[bytes] = None) -> None:
    full_screenshot_data = cls.get_screenshot_as_png()
    screenshots = cls.get_file(full_screenshot_data, log, additional_screenshot_data)

    for filename, data in screenshots:
        cls.save_file(data, cls.get_folder(), filename + '.png', AttachmentType.PNG, 'wb')


def handle_fail(driver) -> None:
    driver.save_xml()
    driver.save_screenshot()