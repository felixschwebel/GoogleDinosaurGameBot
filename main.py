from botplayer import DinosaurGameBot

bot = DinosaurGameBot()
game_is_on = True

while game_is_on:
    if bot.detect_obstacles():
        bot.jump()



