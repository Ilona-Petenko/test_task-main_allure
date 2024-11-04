
import subprocess
import time

import pytest
from appium import webdriver


from utils.android_utils import android_get_desired_capabilities
from appium.options.android import UiAutomator2Options
from framework import Logger


def pytest_addoption(parser: pytest.Parser, pluginmanager):
    parser.addoption('--color_logs', action='store_true', default=False, help='Color logs')


def pytest_configure(config: pytest.Config) -> None:
    Logger.setup(config.option.color_logs)


@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
    #     stdout=subprocess.DEVNULL,
    #     stderr=subprocess.DEVNULL,
    #     stdin=subprocess.DEVNULL,
    #     shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def driver():
    options = UiAutomator2Options()
    options.load_capabilities(android_get_desired_capabilities())
    driver = webdriver.Remote('http://localhost:4723', options=options)
    yield driver
    driver.quit()
