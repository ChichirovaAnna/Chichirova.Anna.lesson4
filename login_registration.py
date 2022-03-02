import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Registration_login: регистрация аккаунта
driver = webdriver.Chrome("C:\chromedriver")
driver.maximize_window()
time.sleep(5)
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
MyAccount = driver.find_element_by_link_text("My Account")
MyAccount.click()
reg_email = driver.find_element_by_id("reg_email")
reg_email.send_keys("1@2.ru")
time.sleep(5)
reg_password = driver.find_element_by_id("reg_password")
reg_password.send_keys("Auto2022matioN")
wait = WebDriverWait(driver, 10)
Strong = wait.until(
    EC.text_to_be_present_in_element(
        (By.XPATH, "//div[@aria-live='polite']"), "Strong")
    )
register = driver.find_element_by_xpath("//input[@name='register']")
register.click()

#Registration_login: логин в систему
driver.execute_script("window.open();")
window_login_sis = driver.window_handles[1]
driver.switch_to.window(window_login_sis)
driver.get("http://practice.automationtesting.in/")
MyAccount = driver.find_element_by_link_text("My Account")
MyAccount.click()
username = driver.find_element_by_id("username")
username.send_keys("1@2.ru")
password = driver.find_element_by_id("password")
password.send_keys("Auto2022matioN")
wait = WebDriverWait(driver, 10)
login = driver.find_element_by_xpath("//input[@name='login']")
login.click()
Logout = wait.until(
    EC.text_to_be_present_in_element(
        (By.XPATH, "//*[@class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout']/a"), "Logout"
    ))

