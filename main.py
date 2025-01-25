from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#setting up browser for automation
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

#adding the web url and creating automation
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

#run time loop of 2 min for clicking
timeout_at = 120 #sec
buy_duration = 7 #sec

button = driver.find_element(By.ID,"cookie")
while True:
    start_time = time.time()
    while time.time() - start_time < timeout_at:
        button.click()

    time.sleep(buy_duration)
