from pynput.keyboard import Key, Controller
import time
import random

keyboard = Controller()

time.sleep(2)

foo = ['a', 'b', 'c', 'd']

while True:
    n = random.randrange(30, 60)
    for char in "its spam time":
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    
    
    
