import pyautogui
import time
import math

# Set the duration and interval
duration = 999999999999999999999999999999999999999999999999999999999999999999999999999999

interval = 0.01  # seconds

# Circle parameters
radius = 50  # pixels
center_x, center_y = pyautogui.position()  # starting position

# Start time
start_time = time.time()

while time.time() - start_time < duration:
    # Calculate the current angle based on elapsed time
    elapsed_time = time.time() - start_time
    angle = 2 * math.pi * (elapsed_time % 1)  # complete circle every 1 second

    # Calculate the new cursor position
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)

    # Move the cursor to the new position
    pyautogui.moveTo(x, y)

    # Wait for the next interval
    time.sleep(interval)
        
