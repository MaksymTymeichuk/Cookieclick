from selenium import webdriver
from selenium.webdriver.common.by import By

import time
def main():
    
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    search_input = driver.find_element_by_name("q")
    searh_input = driver.find_element(By.NAME, "q")
    search_input.send_keys("python\n")
    time.sleep(30)
if __name__ == '__main__':
    main()