import pyautogui
import time

# Function to perform mouse click at given x, y coordinates
def click(x, y):
    pyautogui.click(x, y)
    time.sleep(0.7)  # Wait for one second after the click

# Define the coordinates for each profile
profile_coordinates = {
    #'ALL': (1063, 286),
    'JHACS-GSS': (1054, 305),
    'JHADMREG': (1054, 326),
    'JHCP': (1024, 346),
    'JHHCG-PHQ': (1027, 372),
    'JHHR': (1036, 390),
    'JHHS': (1038, 409)
}

# Function to select profile based on given coordinates
def select_profile(profile_name):
    if profile_name in profile_coordinates:
        click(*profile_coordinates[profile_name])
    else:
        print(f"Profile {profile_name} not found in the coordinates dictionary.")
    time.sleep(2)
# Function to edit hyperfind
def edit_hyperfind(hyperfinds):
    for hyperfind in hyperfinds.split('#'):
        if hyperfind:  # Check if hyperfind is not empty
            click(1040, 389)  # Click to focus the input field
            time.sleep(1.5)
            pyautogui.typewrite(hyperfind)  # Type the hyperfind
            time.sleep(0.5)
            click(1205, 391)
            time.sleep(2)
            click(1035, 435)
            time.sleep(0.5)
            click(1300, 481)
            time.sleep(0.5)
            click(1040, 389)
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'a')  # Select all text
            time.sleep(0.5)
            pyautogui.press('backspace')  # Delete selected text
            time.sleep(0.5)
            pyautogui.press('*')
            time.sleep(1.5)
# Function to finalize the process
def finalize():
    click(1081, 222)  # Finalize the process
    time.sleep(0.7)

# Read the data from HyperfindSorted.txt
with open('profileentry.txt', 'r') as file:
    lines = file.readlines()

# Process each line in the file
for line in lines:
    profile, hyperfinds = line.strip().split(',')
    select_profile(profile.strip())  # Strip to remove any leading/trailing whitespace
    edit_hyperfind(hyperfinds.strip())
    finalize()
    time.sleep(2)  # Sleep for a second before moving to the next line

print("Automation completed.")
