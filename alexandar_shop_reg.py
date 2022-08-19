from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
driver = Chrome()
driver.get("https://www.alexandar-cosmetics.com/en/")
driver.maximize_window()

### input data of registered user

def shop_registered_user(email,password):
    driver.get("https://www.alexandar-cosmetics.com/en/")
    login = driver.find_element(By.XPATH,"/html/body/header/div/div/div[3]/div[4]/div[1]").click()
    time.sleep(2)
    email = driver.find_element(By.XPATH,"//*[@id='username']").send_keys(email)
    time.sleep(2)
    password = driver.find_element(By.XPATH,"//*[@id='password']").send_keys(password)
    time.sleep(2)
    submit = driver.find_element(By.XPATH,"//*[@id='_submit']").click()

### choose productd
    driver.execute_script("window.scrollBy(0,1000)","")
    product = driver.find_element(By.XPATH,"//*[@id='product-slider-2-1']/div/div/div/div[8]/div[4]/div[1]/a").click()
    time.sleep(2)
    add_to_cart = driver.find_element(By.XPATH,"//*[@id='product-detail-page-content']/div/div[2]/div[3]/div[3]/div[2]/div[2]/button").click()
    time.sleep(2)
    cart = driver.find_element(By.XPATH,"/html/body/header/div/div/div[3]/div[3]/div/a/span").click()
    time.sleep(5)
    order = driver.find_element(By.XPATH,"//button[@class='btn order-button cart-order']").click()
    time.sleep(5)

### complete order

    final = driver.find_element(By.XPATH,"//*[@id='checkout-button']").click()   

### final messsage

    if (driver.find_element(By.XPATH,"//*[@id='main-content']/div/div/div/div/div/div/div[2]/div[1]")).is_displayed():
        print("You have successfully placed an order!")
    else:
        print("Order is not successfully completed")

def login_test():
    data = open("data_shop_reg.txt","r").readlines()
    data= [tuple(d.strip().split(","))for d in data]
    for (email,password) in data:
        shop_registered_user(email, password)  
login_test()

