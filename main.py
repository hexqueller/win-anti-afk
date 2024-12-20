import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Controller as MouseController

minutes = 2
iteract_time = int(60 * minutes)

def prevent_sleep():
    keyboard = KeyboardController()
    mouse = MouseController()
    
    while True:
        current_position = mouse.position
        mouse.position = (current_position[0] + 10, current_position[1] + 10)
        time.sleep(0.1)
        mouse.position = current_position
        
        keyboard.press(Key.ctrl_r)
        keyboard.release(Key.ctrl_r)
        
        time.sleep(iteract_time)

if __name__ == "__main__":
    try:
        prevent_sleep()
    except KeyboardInterrupt:
        pass
