from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import Service
import time as t
Chrome_path = r"Chrome driver location"
s = Service(Chrome_path)
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=s)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()
store = driver.find_elements(By.CSS_SELECTOR,".grayed b")
while True:
    interrupt_time = t.time() + 1
    while interrupt_time>t.time():
        cookie = driver.find_element(By.ID,"cookie")
        cookie.click()
    affordable_items = driver.find_elements(By.CSS_SELECTOR,"#store :not(.grayed) b")
    if affordable_items:
        affordable_items[-1].click()
