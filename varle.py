from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

def initialize_webdriver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    return driver, wait

def accept_cookies(driver):
    cookie_button = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    cookie_button.click()


def search_product(driver):
    search_bar = driver.find_element(By.CSS_SELECTOR, 'input[name="q"][type="text"][placeholder="Paieška"]')
    search_bar.send_keys("išmanusis laikrodis")
    search_bar.send_keys(Keys.ENTER)


def scroll_page(driver):
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, -800);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, -400);")
    time.sleep(0.5)
    driver.execute_script("window.scrollBy(0, 800);")
    driver.get("https://www.varle.lt/ismanieji-laikrodziai/ismanusis-laikrodis-garmin-fenix-8-51-mm-amoled--38463957.html")



def search_xmas_present():
    driver, wait = initialize_webdriver()
    driver.get("https://www.varle.lt")
    accept_cookies(driver)
    search_product(driver)
    scroll_page(driver)
    time.sleep(1000)

search_xmas_present()