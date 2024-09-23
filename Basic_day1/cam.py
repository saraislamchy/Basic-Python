import pyautogui
import time

def draw_pyramid(height):
    # Set initial position (you may need to adjust these values)
    start_x, start_y = 500, 500  # Starting position on the screen
    line_height = 20  # Distance between lines
    
    pyautogui.moveTo(start_x, start_y)
    
    for i in range(1, height + 1):
        line = "#" * i
        pyautogui.typewrite(line)
        pyautogui.press('enter')
        time.sleep(0.2)  # Small delay to see the drawing process

    # Print the number of leading spaces before the first `#` in the last line
    print(0)

if __name__ == "__main__":
    height = int(input("Enter the height of the pyramid: "))
    time.sleep(5)  # Give the user 5 seconds to switch to the drawing application
    draw_pyramid(height)
