import pyautogui
import time

# Modified function to perform the sequence of actions with dynamic text input
def automate_actions(text):
    # Clicks on coordinates (1015, 219)
    pyautogui.click(1015, 219)
    time.sleep(1)  # Wait for a second
    
    # Clicks on coordinates (116, 250)
    pyautogui.click(1116, 250)
    time.sleep(1)  # Wait for a second
    
    # Enter the line content instead of fixed "schedule group text"
    pyautogui.write(text)
    time.sleep(1)  # Wait for a second
    
    # Clicks on coordinates (978, 281)
    pyautogui.click(987, 281)
    time.sleep(1)  # Wait for a second
    
    # Clicks on coordinates (1066, 218)
    pyautogui.click(1066, 218)
    time.sleep(1)  # Wait for a second

# Path to the file
file_path = 'C:/Users/omalomo3/Desktop/Hyperfinds Automation/Schedule Group Scripts/ScheduleGroupContent.txt'

# Reading each line from the file and performing the actions
with open(file_path, 'r') as file:
    for line in file:
        # Strip the newline character from the line content
        line_content = line.strip()
        # For each line in the file, perform the sequence of actions with the line content
        automate_actions(line_content)
        # Optional: wait between processing of each line if needed
        time.sleep(2)
