'''
Resources:
https://www.w3schools.com/python/python_datetime.asp
https://www.geeksforgeeks.org/how-to-detect-if-a-specific-key-pressed-using-python/
'''

import keyboard
import datetime

def keylogger():
    while True:
        key_press = keyboard.read_event()  # get the key object
        
        if key_press.name == "esc":
            break  # exit program if escape is pressed
        
        if key_press.event_type == keyboard.KEY_DOWN:
            print(f"[{datetime.datetime.now()}]: {key_press.name}")

keylogger()