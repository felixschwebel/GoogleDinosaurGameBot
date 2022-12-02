# GoogleDinosaurGameBot

A project using the selenium web driver and the Python Imaging Library PIL Fork Pillow. 

To use the code you have to **use the web driver for Chrome** because the game is directly launched from the browser.

<img width="625" alt="Screenshot 2022-12-02 at 21 44 24" src="https://user-images.githubusercontent.com/111788725/205382778-45e4e31f-3547-4b91-9e0b-4d75c6d31cc9.png">

I decided to use a class for the GameBot to I could specify some methods for the bot. In the init-function the web driver is started. Unfortunately an error occurs after the game is launched, I assume because the URL doesn't refer to a real web address. That's why I used the exception handling to continue after the WebDriverException is raised. The game is started by pressing the space bar. Then it waits for 4 seconds using the time module before the bot starts.

<img width="564" alt="Screenshot 2022-12-02 at 21 53 43" src="https://user-images.githubusercontent.com/111788725/205384437-f489edfb-460f-48fe-9d07-c666f856c123.png">

I used the ImageGrab from PIL to grab a little piece of the screen right above the ground but just as high that it doesn’t detect the high-flying birds. The values that I got came from trying. To see if there’s an obstacle the colors of the snippet are checked for dark grey _(172, 172, 172)_. 

<img width="355" alt="Screenshot 2022-12-02 at 21 58 05" src="https://user-images.githubusercontent.com/111788725/205385024-0128ef06-ef1c-4999-8d6f-275e49346292.png">

When an obstacle is detected the jump function is triggered. I decided to not use the ducking functionality because I would have to check for the lower ground and the middle ground separately. This would slow down the checking process and the reaction time of the Dino. I just used the _ARROW-DOWN_ to get the Dino faster back on the ground. Because the speed of the game is changing with time, this switched from a 0.19 s wait to a 0.16 s wait after 50 seconds. 

<img width="327" alt="Screenshot 2022-12-02 at 22 02 51" src="https://user-images.githubusercontent.com/111788725/205385639-be50d2f3-b9f9-4afb-9877-23d6afb69b74.png">
