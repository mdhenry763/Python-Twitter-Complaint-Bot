from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import time

class InterSpeedTwitter:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go_btn = self.driver.find_element(By.CSS_SELECTOR, ".start-text")
        go_btn.click()
        time.sleep(40)
        self.up = self.driver.find_element(
            By.CSS_SELECTOR,
            '.download-speed').text
        self.down = self.driver.find_element(
            By.CSS_SELECTOR,
            '.upload-speed').text
        print(f"down: {self.up}")
        print(f"down: {self.down}")

    def tweet_at_provider(self, email, password):
        self.driver.get('https://twitter.com/compose/tweet')
        time.sleep(10)
        email_input = self.driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/"
            "div[5]/label/div/div[2]/div/input"
        )
        #
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)
        time.sleep(2)
        try:
            password_input = self.driver.find_element(
                By.XPATH,
                "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/"
                "div[3]/div/label/div/div[2]/div[1]/input"
            )
        except NoSuchElementException:
            print("Unsuccessful")
            username_input = self.driver.find_element(
                By.XPATH,
                "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/"
                "div[2]/label/div/div[2]/div/input"
            )
            username_input.send_keys("Michael71880463")
            username_input.send_keys(Keys.ENTER)
            time.sleep(2)
            password_input = self.driver.find_element(
                By.XPATH,
                "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div"
                "/div/div[3]/div/label/div/div[2]/div[1]/input"
            )

        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(50)
        tweet_box = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/"
            "div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div"
        )
        tweet_box.click()
        if int(self.down) < 100:
            tweet_box.send_keys(f"@MWEBTweets, why is my internet speed{self.down}down/"
                                f"{self.up}up when we pay for 200down/50up")
            time.sleep(3)
            tweet_btn = self.driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]"
                "/div[3]/div/div/div[2]/div[3]"
            )
            tweet_btn.click()
        else:
            tweet_box.send_keys(f"@MWEBTweets, thank you my internet speed{self.down}down/"
                                f"{self.up}up when we pay for 200down/50up")
            time.sleep(3)
            tweet_btn = self.driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]"
                "/div[3]/div/div/div[2]/div[3]"
            )
            tweet_btn.click()


        # //*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input
        # input
        #/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input
        # password
        # /html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div
        # button