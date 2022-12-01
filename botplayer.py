import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image, ImageGrab
import time
import os

chrome_webdriver = os.environ["CHROME_DRIVER"]
URL = "chrome://dino"


class DinosaurGameBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_webdriver)

        # Catch the WebDriverException that's returned because of the Chrome URL
        try:
            self.driver.get(URL)
        except selenium.common.exceptions.WebDriverException:
            pass
        # Start the game with the space bar after 2 seconds
        time.sleep(2)
        self.body = self.driver.find_element(By.TAG_NAME, 'body')
        self.body.send_keys(Keys.SPACE)

    def jump(self):
        self.body.send_keys(Keys.ARROW_UP)

    def duck(self):
        self.body.send_keys(Keys.ARROW_DOWN)

    def get_frame(self):
        # bbox (xmin, ymin, xmax, ymax)
        box = ImageGrab.grab(bbox=(350, 450, 500, 650))
        return box

