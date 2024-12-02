import time
from pynput.mouse import Controller

def move_mouse():
    mouse = Controller()
    while True:
        current_position = mouse.position

        mouse.position = (current_position[0] - 1, current_position[1])
        time.sleep(0.1)

        mouse.position = (current_position[0], current_position[1])
        print(f"Mouse moved to: {mouse.position}")
        time.sleep(10)

if __name__ == "__main__":
    try:
        move_mouse()
    except KeyboardInterrupt:
        pass
