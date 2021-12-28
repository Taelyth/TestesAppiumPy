from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_capabilities = dict(
    platformName='Android',
    platformVersion='11',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.google.android.calculator',
    appActivity='com.android.calculator2.Calculator'
)

desired_capabilities_real = dict(
    platformName='Android',
    platformVersion='10',
    automationName='uiautomator2',
    deviceName='motorola one',
    appPackage='com.google.android.calculator',
    appActivity='com.android.calculator2.Calculator'
)


def teste_appium():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities_real)
    # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities_real)

    driver.implicitly_wait(2)

    btn7 = driver.find_element(AppiumBy.ID, 'com.google.android.calculator:id/digit_7')
    btn5 = driver.find_element(AppiumBy.ID, 'com.google.android.calculator:id/digit_5')
    btnsoma = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'mais')
    btnigual = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'igual')

    btn7.click()
    btnsoma.click()
    btn5.click()
    btnigual.click()

    resultado = driver.find_element(AppiumBy.ID, 'com.google.android.calculator:id/result_final').text

    assert resultado == '12'
    driver.quit()
