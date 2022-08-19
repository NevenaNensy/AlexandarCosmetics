from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def new_user(f_name,l_name,birth,email,password,password_conf):
    driver = Chrome()
    driver.get("https://www.alexandar-cosmetics.com/en/")
    login = driver.find_element(By.XPATH,"/html/body/header/div/div/div[3]/div[4]/span")
    login.click()
    time.sleep(5)
    register = driver.find_element(By.XPATH,"/html/body/header/div/div/div[3]/div[4]/div[2]/div[2]/button[2]")
    register.click()
    time.sleep(5)

    gender = driver.find_element(By.XPATH,"//*[@id='user-gender']")
    gender.click()
    gender.send_keys("female")
    gender.click()
    first_name = driver.find_element(By.XPATH,"//*[@id='first-name']")
    first_name.send_keys(f_name)
    last_name = driver.find_element(By.XPATH,"//*[@id='last-name']")
    last_name.send_keys(l_name)
    birthday = driver.find_element(By.XPATH,"//*[@id='date-of-birth']")
    birthday.send_keys(birth)
    e_mail = driver.find_element(By.XPATH,"//*[@id='email']")
    e_mail.send_keys(email)
    passw = driver.find_element(By.XPATH,"//*[@id='register-password']")
    passw.send_keys(password)
    passw_confirmation = driver.find_element(By.XPATH,"//*[@id='register-password-confirmation']")
    passw_confirmation.send_keys(password_conf)
    time.sleep(5)
    register_submit = driver.find_element(By.XPATH,"//*[@id='register-submit']")
    time.sleep(10)
    register_submit.click()
    time.sleep(5)
    if (driver.find_element(By.XPATH,"//*[@id='register-modal-success-text']").is_displayed()):
        print("Login sucess")
    else:
        print("Login failed")    

    time.sleep(40)

def login_test():
    data_a = open("data_alredy_registred.txt","r").readlines()
    data_a= [tuple(d.strip().split(","))for d in data_a]
    for (f_name,l_name,birth,email,password,password_conf) in data_a:
        new_user(f_name, l_name, birth, email, password, password_conf)   
login_test()
