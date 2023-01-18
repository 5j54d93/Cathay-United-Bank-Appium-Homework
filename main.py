from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from appium import webdriver
import os

def screenshot(driver, fileName):
    driver.save_screenshot(os.getcwd() + '/' + fileName)

def waitAndClick(driver, By, string):
    wait.until(EC.presence_of_element_located((By, string)))
    driver.create_web_element(driver.find_element(By, string)["ELEMENT"]).click()

desiredCapabilities = {
    'platformName': 'Android',
    'platformVersion': '12',
    'deviceName': '172.25.137.138:5555',
    'automationName': 'UiAutomator2',
    'browserName': 'Chrome'
}
driver = webdriver.Remote('http://localhost:4725/wd/hub', desiredCapabilities)
driver.get('https://www.cathaybk.com.tw/cathaybk/')
wait = WebDriverWait(driver, 60)

wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cubre-o-quickLink')))
screenshot(driver, 'home page.png')

waitAndClick(driver, By.CLASS_NAME, 'cubre-o-header__burger')
waitAndClick(driver, By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]')
waitAndClick(driver, By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[1]')
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cubre-o-menuLinkList__content")))
screenshot(driver, 'credit card list.png')

creditCardList = driver.create_web_element(driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]")["ELEMENT"])
print("-----")
print("There are " + str(len(creditCardList.find_elements(By.XPATH, './/a[@class="cubre-a-menuLink"][@id="lnk_Link"]'))) + " rows in credit card menu.")
waitAndClick(driver, By.XPATH, '//*[@id="lnk_Link"]')
waitAndClick(driver, By.XPATH, '/html/body/div[1]/main/article/div/div/div/div[1]/div/div/a[3]')
waitAndClick(driver, By.XPATH, '/html/body/div[1]/main/article/div/div/div/div[1]/div/div/a[5]')
waitAndClick(driver, By.XPATH, '/html/body/div[1]/main/article/div/div/div/div[1]/div/div/a[6]')
bulletsArea = driver.create_web_element(driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]")["ELEMENT"])
bullets = bulletsArea.find_elements(By.XPATH, './/span[@role="button"]')
print("-----")
print("There are " + str(len(bullets)) + " credit cards that stop contribute.")

for idx, bullet in enumerate(bullets):
    creditCard = driver.create_web_element(bullet["ELEMENT"])
    creditCard.click()
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[1]/div[" + str(idx + 1) + "]")))
    screenshot(driver, 'credit card - ' + str(idx + 1) + '.png')

numOfCreditCardImg = 0
for path in os.listdir(os.getcwd()):
    if os.path.isfile(os.path.join(os.getcwd(), path)) and path.startswith("credit card - "):
        numOfCreditCardImg += 1

print("-----")
if numOfCreditCardImg == len(bullets):
    print("Number of credit card screenshot is the same as website.")

driver.quit()