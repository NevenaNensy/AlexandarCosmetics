from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
driver = Chrome()
driver.get("https://www.alexandar-cosmetics.com/en/")
driver.maximize_window()

### order product like guestC
driver.implicitly_wait(10)
driver.execute_script("window.scrollBy(0,1000)","")
product = driver.find_element(By.XPATH,"//*[@id='product-slider-2-1']/div/div/div/div[7]/div[4]/div[1]/a")
time.sleep(2)
product.click()
add_to_cart = driver.find_element(By.CSS_SELECTOR,"#product-detail-page-content > div > div.product-description.main-product-description.col-xs-12.col-sm-6 > div:nth-child(3) > div.add-to-cart.form-inline.add-to-cart-ajax.resettable > div.add-to-cart-container > div.add-to-cart-button > button > em")
time.sleep(5)
add_to_cart.click()
time.sleep(5)
order = driver.find_element(By.XPATH,"//span[@class='badge quantity number-font cart_count_display']")
time.sleep(2)
order.click()
final_order = driver.find_element(By.XPATH,"/html/body/main/div/div/div[3]/div[4]/div/div[1]/div/div[5]/button")
final_order.click()

### choose guest mode

continue_as_quest = driver.find_element(By.XPATH,"//*[@id='continue-as-guest']")
time.sleep(5)
continue_as_quest.click()
time.sleep(5)

### data of shipping address

name = driver.find_element(By.XPATH,"//*[@id='createCheckoutStep1_newAddress_guestFirstName']")
name.send_keys("test name")
last_name = driver.find_element(By.XPATH,"//*[@id='createCheckoutStep1_newAddress_guestLastName']")
last_name.send_keys("test last name")
emai = driver.find_element(By.XPATH,"//*[@id='createCheckoutStep1_newAddress_guestEmail']")
emai.send_keys("test1@gmail.com")
street = driver.find_element(By.XPATH,"//*[@id='createCheckoutStep1_newAddress_streetAddress']")
street.send_keys("test street")
postal_code = driver.find_element(By.XPATH,"//*[@id='createCheckoutStep1_newAddress_postalCode']")
postal_code.send_keys("34000")
time.sleep(5)
postal_code.send_keys(Keys.ARROW_DOWN)
time.sleep(5)
postal_code.send_keys(Keys.ENTER)
time.sleep(2)
phone = driver.find_element(By.XPATH,"//*[@id='createCheckoutStep1_newAddress_phone']")
phone.send_keys("454557845")
next_page1 = driver.find_element(By.XPATH,"//*[@id='checkout-form-resize-mob']/div[2]/div/div[2]/div/button[1]")
next_page1.click()

### choose where to pickup

pickup = driver.find_element(By.XPATH,"//*[@id='createCheckoutStep2_shipping']/label[2]/div[2]/div[1]")
pickup.click()
next_page2 = driver.find_element(By.XPATH,"//*[@id='checkout-focus']/div[2]/div/button[1]")
next_page2.click()
check = driver.find_element(By.XPATH,"//input[@type='radio']")
check.click()
next2 = driver.find_element(By.XPATH,"//*[@id='checkout-focus']/div[2]/div/button[1]")
time.sleep(5)
next2.click()

### payment method

payment = driver.find_element(By.XPATH,"//*[@id='createCheckoutStep3_payment_2']")
time.sleep(2)
payment.click()
next3 = driver.find_element(By.XPATH,"//*[@id='checkout-focus']/div[2]/div/button[1]")
time.sleep(2)
next3.click()

### complete order

complete_order = driver.find_element(By.XPATH,"//*[@id='checkout-button']")
time.sleep(5)
complete_order.click()
time.sleep(5)

### expected and actual message
# assertion

if (driver.find_element(By.XPATH,"//*[@id='main-content']/div/div/div/div/div/div/div[2]/div[1]")).is_displayed()==True:
    print("You have successfully placed an order!")
else:
    print("Order is not successfully completed")

assert driver.find_element(By.XPATH,"//*[@id='main-content']/div/div/div/div/div/div/div[2]/div[1]").is_displayed()==True