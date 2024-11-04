
import subprocess
import re


def android_get_desired_capabilities():
    result = subprocess.check_output("adb devices", shell=True).decode().strip()

    pattern = re.compile(r'(\S+)\s+device$')
    udid = re.findall(pattern, result)

    res = {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8302,
        'takesScreenshot': True,
        'udid': udid[0],
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }
    return res
