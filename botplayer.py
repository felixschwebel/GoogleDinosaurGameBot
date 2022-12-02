import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import ImageGrab
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
        time.sleep(4)
        self.time = time.time()

    def jump(self):
        self.body.send_keys(Keys.ARROW_UP)
        if time.time() > self.time + 50:
            time.sleep(0.16)
        else:
            time.sleep(0.19)
        self.body.send_keys(Keys.ARROW_DOWN)

    def detect_obstacles(self):
        # bbox (xmin, ymin, xmax, ymax)
        # Get the values for the grab-box by trying
        xmax = 335
        width = 65
        ymax = 620
        height = 80
        box = ImageGrab.grab(bbox=(xmax-width, ymax-height, xmax, ymax))
        colors = [color[1] for color in box.getcolors()]
        if (172, 172, 172, 255) in colors:
           return True
        else:
           return False

