from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import presence_of_element_located



driver = webdriver.Chrome('/home/home/ch_dr/chromedriver')
wait=WebDriverWait(driver,10)
driver.get("http://www.globallogic.com/ua/careers/")
search_field= driver.find_element_by_id('by_keyword')
search_field.clear()
search_field.send_keys('QA'+Keys.RETURN)
wait.until(presence_of_element_located((By.CSS_SELECTOR, ".filter-main")))
search_result = driver.find_elements(By.XPATH, "//div[contains(@class,'career-searchpage')]//div[@class='row']//div[@class='career-pagelink']")
result = search_result[0].find_element_by_class_name("mb-0")
print(result.text)


