from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

time.sleep(2)
five_min = time.time() + 60*5
shop_timeout = time.time() + 5
while time.time() < five_min:
    cookie.click()
    if time.time() > shop_timeout:
        money = driver.find_element(By.ID, "money")
        player_coins = money.text.replace(",", "")  # Remove commas from player_coins
        print(player_coins)
        store = driver.find_element(By.CSS_SELECTOR, value="#store")
        max_price = 0
        store_item = driver.find_element(By.CSS_SELECTOR, value="#store div b")
        bought_something = False
        for item in driver.find_elements(By.CSS_SELECTOR, value="#store div b"):
            print(item.text) # prints price per item in store
            price = item.text.split(" - ")[1]
            item_price = int(price.replace(",", "")) # Remove commas from item price
            if int(player_coins) > item_price:
                max_price = item_price
                store_item = item
            else:
                store_item.click()
                bought_something = True
                break
        if not bought_something:
            store_item.click()
        shop_timeout = time.time() + 5

driver.quit()







