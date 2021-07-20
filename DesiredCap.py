from appium import webdriver
import time
from locelement import LOCELEMENT
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def capabilities():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Nexus S API 26'
    desired_caps['appPackage'] = 'com.google.android.youtube'
    desired_caps['appActivity'] = 'com.google.android.apps.youtube.app.application.Shell$HomeActivity'
    desired_caps['noReset'] = 'true'
    # desired_caps['forceMjsonwp'] = 'true'
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


driver = capabilities()
LOCELEMENT = LOCELEMENT()

#search_text
text = 'Ivan Tay Selenium Automation'
driver.find_element_by_accessibility_id(LOCELEMENT.LOC_NAV_SEARCH_ACC).click()
# Список кодов клавиш:
# a - z- > 29 - 54
# "0" - "9" → 7 - 16
# КНОПКА BACK - 4, КНОПКА МЕНЮ - 82
# UP-19, DOWN-20, LEFT-21, RIGHT-22
# SELECT (СРЕДНЯЯ) КНОПКА - 23
# SPACE - 62, SHIFT - 59, ENTER - 66, BACKSPACE - 67
#после воода текста в строку поиска, надо нажать enter на девайсе

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, LOCELEMENT.LOC_SEARCH_INPUT_ID)))
except TimeoutException:
    print('Timeout. Cannot find this element')
    driver.quit()

driver.find_element_by_id(LOCELEMENT.LOC_SEARCH_INPUT_ID).send_keys(text)
driver.press_keycode(66)

# xpath1 = "//android.support.v7.widget.RecyclerView[@resource-id='com.google.android.youtube:id/results']/android.view.ViewGroup"
#
# try:
#     elements = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath1)))
# except TimeoutException:
#     print('Timeout. Cannot find this element')
#     driver.quit()
# xpath1 = "//android.support.v7.widget.RecyclerView[@resource-id='com.google.android.youtube:id/results']/android.widget.LinearLayout[@resource-id='com.google.android.youtube:id/video_info_view']"

xpath1 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout"

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath1)))
except TimeoutException:
    print('Timeout. Cannot find this element')
    driver.quit()


elements = driver.find_elements_by_xpath(xpath1)
elements[0].click()

time.sleep(4)
driver.find_element_by_xpath(LOCELEMENT.LOC_VIEWER_VIEWER_XPATH).click()
driver.find_element_by_xpath(LOCELEMENT.LOC_VIEWER_VIEWER_XPATH).click()
time.sleep(10)
driver.find_element_by_id(LOCELEMENT.LOC_VIEWER_PLAY_ID).click()
time.sleep(4)

#quit
driver.quit()