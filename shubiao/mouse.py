import pyautogui
import time

def print_mouse_position():
    while True:
        x, y = pyautogui.position()
        print(f"Mouse position: X={x}, Y={y}")
        time.sleep(2)

if __name__ == "__main__":
    print_mouse_position()