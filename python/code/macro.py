import pyautogui as pg
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.reb.or.kr/r-one/main.do"
driver = webdriver.Chrome("/usr/dami/Desktop//Users/dami/Desktop/chromedriver_mac64/chromedriver")
# driver.get()
driver.find_element(By.XPATH, "//*[@id='SEP_10000']/a")
driver.find_element(By.XPATH, "//*[@id='HOUSE_22000']/a")
driver.find_element(By.XPATH, "//*[@id='HOUSE_22100']/a")

driver.switch_to.window(driver.window_handles[-1])

select = Select(driver.find_element(By.ID, "researchYear_s"))
select.select_by_value("2021")
select = Select(driver.find_element(By.ID, "researchMonth_s"))
select.select_by_value("01")

select = Select(driver.find_element(By.ID, "researchYear_s"))
select.select_by_value("2022")
select = Select(driver.find_element(By.ID, "researchMonth_s"))
select.select_by_value("12")