import pyautogui
import time

# Prompt the user to enter the number of times the loop should run
num_iterations = int(input("Enter the number of times to run the loop: "))

for i in range(num_iterations):
    # Perform the first mouse click at (1081, 350)
    pyautogui.click(x=1081, y=390)
    time.sleep(0.25)  # Wait for half a second

    # Perform the second mouse click at (1203, 236)
    pyautogui.click(x=1203, y=236)
    time.sleep(0.25)  # Wait for half a second

    # Perform the third mouse click at (1557, 255)
    pyautogui.click(x=1557, y=255)
    time.sleep(0.25)  # Wait for half a second

    #pyautogui.click(x=44, y=71)
    #time.sleep(0.25)  # Wait for half a second
    #pyautogui.press('down')
    #time.sleep(0.25)
    # Print the current iteration count
    print(f"Loop {i + 1} completed.")

print("All loops completed.")
