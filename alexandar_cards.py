from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()
def test_all_cards():
    driver.get("https://www.alexandar-cosmetics.com/en/")
    cards = ["//*[@id='navbar']/nav/div[2]/ul/li[1]/a/span","//*[@id='navbar']/nav/div[2]/ul/li[2]/a/span","//*[@id='navbar']/nav/div[2]/ul/li[3]/a/span","//*[@id='navbar']/nav/div[2]/ul/li[4]/a/span","//*[@id='navbar']/nav/div[2]/ul/li[5]/a/span","//*[@id='navbar']/nav/div[2]/ul/li[6]/a/span","//*[@id='navbar']/nav/div[2]/ul/li[7]/a/span","//*[@id='navbar']/nav/div[2]/ul/li[8]/a/span","//*[@id='navbar']/nav/div[2]/ul/li[9]/a/span","//*[@id='navbar']/nav/div[2]/ul/li[10]/a/span","//*[@id='navbar']/nav/div[2]/ul/li[11]/a/span","//*[@id='navbar']/nav/div[2]/ul/li[12]/a/span"]
    for c in cards:
        result = driver.find_element(By.XPATH,c)
        result.click()   
    assert driver.find_element(By.LINK_TEXT,"HAIR").is_displayed()==True
    assert driver.find_element(By.LINK_TEXT,"NAILS").is_displayed()==True
    assert driver.find_element(By.LINK_TEXT,"FACE & BODY").is_displayed()==True
    assert driver.find_element(By.LINK_TEXT,"MAKEUP").is_displayed()==True
    assert driver.find_element(By.LINK_TEXT,"FOR MEN").is_displayed()==True
    assert driver.find_element(By.LINK_TEXT,"SALON EQUIPMENT").is_displayed()==True
    assert driver.find_element(By.LINK_TEXT,"BODY ART").is_displayed()==True
    assert driver.find_element(By.LINK_TEXT,"NEW").is_displayed()==True
    assert driver.find_element(By.XPATH,"//span[@itemprop='name']").is_displayed()==True
    assert driver.find_element(By.LINK_TEXT,"BESTSELLERS").is_displayed()==True
    assert driver.find_element(By.LINK_TEXT,"GIFT CARDS").is_displayed()==True

test_all_cards()
    
    
    




