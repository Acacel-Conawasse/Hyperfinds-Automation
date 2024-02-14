import pyautogui
import time

# Coordinates to click
click_coords = [(2053, 553), (1961, 248), (2687, 250)]

# Wait time between clicks
wait_time = 0.5

# Run the loop 100 times
for i in range(100):
    for coord in click_coords:
        pyautogui.click(coord[0], coord[1])
        time.sleep(wait_time)