from selenium import webdriver
import time

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path= "C:/chromedriver",
    options = options
)
try:
    driver.get("https://www.1rnd.ru/news")
    #items = driver.find_elements(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div[4]/div[2]/div[1]/div[1]")
    items = driver.find_elements(by=By.CLASS_NAME, value="c-news-block__head")
    items[0].click()
    #pars = driver.find_element_by_class_name("infinitblock")
    pars = driver.find_element(by=By.CLASS_NAME, value="article-details__text")
    print(pars.text)
    file = open("1.txt","w")
    file.write(pars.text)


   #driver.switch_to.window(driver.window_handles[1])
    driver.back()
    items = driver.find_elements(by=By.CLASS_NAME, value="c-news-block__head")
    #time.sleep(5)
    items[1].click()

    pars1 = driver.find_element(by=By.CLASS_NAME, value="article-details__text")
    print(pars1.text)
    file = open("2.txt", "w")
    file.write(pars1.text)
    driver.back()

    items = driver.find_elements(by=By.CLASS_NAME, value="c-news-block__head")
    items[2].click()
    pars2 = driver.find_element(by=By.CLASS_NAME, value="article-details__text")
    print(pars2.text)
    file = open("3.txt", "w")
    file.write(pars2.text)
    driver.back()

    items = driver.find_elements(by=By.CLASS_NAME, value="c-news-block__head")
    items[3].click()
    pars3 = driver.find_element(by=By.CLASS_NAME, value="article-details__text")
    print(pars3.text)
    file = open("3.txt", "w")
    file.write(pars3.text)
    driver.back()

    items = driver.find_elements(by=By.CLASS_NAME, value="c-news-block__head")
    items[4].click()
    pars4 = driver.find_element(by=By.CLASS_NAME, value="article-details__text")
    print(pars4.text)
    file = open("4.txt", "w")
    file.write(pars4.text)
    driver.back()

finally:
    driver.close()
    driver.quit()
