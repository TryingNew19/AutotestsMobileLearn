from appium import webdriver
import time
from locelement import LOCELEMENT
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

# title_id = "com.google.android.youtube:id/title"
toolbar_id = "com.google.android.youtube:id/toolbar"
def capabilities():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    # desired_caps['deviceName'] = 'Nexus S API 26'
    desired_caps['deviceName'] = '1fca8920'
    desired_caps['appPackage'] = 'com.google.android.youtube'
    # desired_caps['appActivity'] = 'com.google.android.apps.youtube.app.application.Shell$HomeActivity'
    # на xiaomi активити назыв. по-другому
    desired_caps['appActivity'] = 'com.google.android.apps.youtube.app.application.Shell_HomeActivity'
    desired_caps['noReset'] = 'true'
    # desired_caps['forceMjsonwp'] = 'true'
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


driver = capabilities()

# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, title_id)))
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, toolbar_id)))

action = TouchAction(driver)
action.press(None, 0, 750, None).wait(1000).move_to(None, 0, 50).release().perform()

time.sleep(10)
driver.quit()