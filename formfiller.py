from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
URL = "https://docs.google.com/forms/d/e/1FAIpQLSf26LMnrL9nqrTm5tUVvVeyuAvBFCpoznL6fvM7a-G6oAt81g/viewform?usp=sf_link"

class FormFiller():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def fill_out_form(self, prices, links, addrs):
        self.driver.get(URL)
        time.sleep(3)  #  Wait for page to load
        #  Start loop
        index = 0 #  Grab each respective item in the lists
        for price in prices:
            input_box = self.driver.find_elements(By.CSS_SELECTOR, "input[type='text']")  #  Grab all the input boxes
            input_box[0].send_keys(addrs[index])
            input_box[1].send_keys(price)
            input_box[2].send_keys(links[index])
            self.driver.find_element(By.CSS_SELECTOR, "div div span span").click()
            self.driver.find_element(By.CSS_SELECTOR, "div a").click()
            index += 1
        #  End loop

    # def make_sheet(self): #  Selenium opens a non-signed in chrome which is deemed unsecure to sign in on.
    #     self.driver.find_element(By.CSS_SELECTOR, "svg").click()
    #     self.driver.find_element(By.CSS_SELECTOR, "div div div span").click()
    #     self.driver.find_element(By.CSS_SELECTOR, "div div span span").click()
    #     self.driver.find_element(By.XPATH, "//*[@id='yDmH0d']/div[14]/div/div[2]/div[3]/div[2]/span/span").click()  # Create button click


