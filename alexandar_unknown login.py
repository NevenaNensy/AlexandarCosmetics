from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

### Checking if is it possible to log in when a user is not registered 

def test_unknow_user():
    driver = Chrome()
    driver.get("https://www.alexandar-cosmetics.com/en/")
    driver.maximize_window()
    login = driver.find_element(By.XPATH,"/html/body/header/div/div/div[3]/div[4]/span")
    login.click()
    login1 = driver.find_element(By.XPATH,"/html/body/header/div/div/div[3]/div[4]/div[2]/div[2]/button[1]")
    login1.click()
    time.sleep(5)
    unknow_user = driver.find_element(By.XPATH,"//*[@id='username']")
    unknow_user.send_keys("nevena@gmail.com")
    time.sleep(5)
    unknow_passw = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='password']")))
    unknow_passw.click()
    unknow_passw.send_keys("Nevena123")
    submit = driver.find_element(By.XPATH,"//*[@id='_submit']")
    submit.click()
    time.sleep(5)

### actual message

    actual_msg = driver.find_element(By.XPATH,"//*[@id='login-modal']/div/div/div[3]/div/div").text
    expected_msg = "Email is not confirmed"
    print("Expected message: ",expected_msg,"Actual message: ", actual_msg)
    assert expected_msg == actual_msg
    driver.quit()

test_unknow_user()