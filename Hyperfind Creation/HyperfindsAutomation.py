import sys
import pyautogui
import time
import logging
import pyperclip

"""
Read Me: 

Book Mark Bar needs to be allowed in firefox 
PC screen resolution in display settings needs to be set to 100% 
FireFox screen size needs to be set to 100%
Finally your input file path ** All the way at the bottom should be / as to \
Use your laptop only no docks 
VS code to the left
Firefox to the right <evenly split screen>
"""


# Setup logging to keep track of actions
logging.basicConfig(filename="log.txt", level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
pyautogui.FAILSAFE = True  # Enable failsafe by moving the mouse to the upper left corner


def move_and_click(x, y, clicks=1, button='left'):
    """Moves the mouse to a specified location and performs a click."""
    pyautogui.moveTo(x, y)
    pyautogui.click(clicks=clicks, button=button)
    time.sleep(0.02)  # Adjusted to the actual wait time
    #logging.info(f"Mouse moved and clicked at ({x}, {y}), with a 0.20 second interval")

def enter_text(text):
    """Enters text at the current cursor location."""
    pyautogui.write(text, interval=0.01)
    #logging.info(f"Entered text: {text}")

def start_hyperfind_creation():
    """Starts the creation of a new Hyperfind."""
    move_and_click(1007, 240)
    time.sleep(0.5)
    move_and_click(1338, 263)
    time.sleep(0.2)
    move_and_click(1338, 263)
    time.sleep(0.5)

def enter_hyperfind_details(hyperfind_name, description):
    """Enters Hyperfind name and description."""
    move_and_click(1065, 220)
    time.sleep(0.04)
    enter_text(hyperfind_name)
    move_and_click(1044, 254)
    time.sleep(0.05)
    move_and_click(1044, 254)
    enter_text(description)

def add_hyperfind_condition():
    """Navigates to add a new condition for the Hyperfind."""
    move_and_click(1420, 511)
    time.sleep(2)

def select_primary_labor_category():
    """Selects the primary labor category."""
    move_and_click(1077, 411)
    time.sleep(2)
    move_and_click(1012,252)
    time.sleep(0.05)


def select_and_add_plc_items(plc_type, plc_items):
    """Selects a PLC type and adds items to it."""
    plc_coordinates = {
        "CostCenter": (1318, 321),
        "OrgUnit": (1798, 287),
    }
    x, y = plc_coordinates[plc_type]
    move_and_click(x, y)
    time.sleep(0.20)  # Wait for the selection to take effect

    add_plc_items(plc_items)
    move_and_click(1445,772)
    time.sleep(0.05)

def add_plc_items(plc_items):
    """Adds items to the selected PLC type."""
    for item in plc_items:
        if '*' in item:
            # Special handling for items containing '*'
            move_and_click(1425, 372)
            time.sleep(0.05)
            enter_text(item.strip(' '))
            time.sleep(0.05)
            move_and_click(1697, 372)
            time.sleep(0.05)

        else:
            move_and_click(1310, 453)
            time.sleep(0.05)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.05)
            pyautogui.press('backspace')
            enter_text(item.strip())
            move_and_click(1343, 482)
            time.sleep(0.05)
            move_and_click(1589, 493)
            time.sleep(0.5)

def employment_status_steps():
    """Performs additional steps if employment status is 'Y'."""
    move_and_click(1010, 296)
    time.sleep(0.5)
    move_and_click(1057, 374)
    time.sleep(0.5)
    move_and_click(1010, 293)
    time.sleep(0.5)
    move_and_click(1445,772)
    time.sleep(0.5)


def schedule_group_steps(schedule_group_text):
    """Performs additional steps if Schedule Group is not 'Null'."""
    if schedule_group_text != "Null":
        move_and_click(1031,453)
        time.sleep(0.5)
        move_and_click(1050,494)
        time.sleep(0.5)
        move_and_click(1031,453)
        time.sleep(0.5)
        move_and_click(1332,346)
        time.sleep(0.5)
        # Enter Schedule group keystrokes
        enter_text(schedule_group_text)
        time.sleep(0.5)
        move_and_click(1511,344)
        time.sleep(0.5)
        move_and_click(1364,380)
        time.sleep(0.5)
        move_and_click(1592,386)
        time.sleep(0.5)
        move_and_click(1455,772)
        time.sleep(0.5)
        

def finalize_hyperfind_creation(hyperfind_name, orgunit, cost_centers):
    """Finalizes and saves the Hyperfind."""
    #move_and_click(1417, 777)
    time.sleep(2.5)
    move_and_click(1864, 988)
    time.sleep(2)
    """iuhu"""
    # Click to focus and select the item, and copy it to the clipboard
    pyautogui.click(1194, 318)
    time.sleep(0.1)
    pyautogui.click(1194, 318)
    time.sleep(0.1)
    pyautogui.click(1194, 318)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)  # Wait a bit for the clipboard to update

    # Retrieve and process the copied text
    copied_text = pyperclip.paste()
    copied_numbers = set(''.join(filter(str.isdigit, copied_text)).split(','))
    if cost_centers != "Null":
        expetedConditions = set(''.join(filter(str.isdigit, cost_centers)).split('#'))
    if orgunit !="Null":
        expetedConditions = set(''.join(filter(str.isdigit,orgunit)).split('#'))
        

    # Compare the two sets of numbers
    if copied_numbers == expetedConditions:
        time.sleep(2)
        move_and_click(1786, 994)
        time.sleep(2.5)
        print ("All items match.")
    else:
        # Log the unmatched items
        with open("unsure_costcenters.txt", "a") as file:
            file.write("\n"+"Unmatched items found. First element: {}\n".format(next(iter(copied_numbers))))
            file.write(hyperfind_name +" not created"+ "\n")
            file.write("-----------------------------------------------------------------")
        print(hyperfind_name +"not created")
        pyautogui.click(1711, 993)  # click cancel
        time.sleep(1)
        pyautogui.press('tab', presses=2, interval=0.09)
        time.sleep(.25)
        pyautogui.press('enter')
        time.sleep(.5)



def process_hyperfind(hyperfind_name, description, cost_centers, orgunit, employment_status, schedule_group,):
    """Processes each hyperfind entry."""
    start_hyperfind_creation()
    enter_hyperfind_details(hyperfind_name, description)
    add_hyperfind_condition()
    select_primary_labor_category()

    if cost_centers != "Null":
        select_and_add_plc_items("CostCenter", cost_centers.split('#'))

    if orgunit != "Null":
        select_and_add_plc_items("OrgUnit", orgunit.split('#'))

    # Check employment status and perform additional steps if 'Y'
    if employment_status == "Y":
        employment_status_steps()

    # Perform additional steps for Schedule Group
    schedule_group_steps(schedule_group)

    finalize_hyperfind_creation(hyperfind_name, orgunit, cost_centers)
    return f"{hyperfind_name}: Processed Successfully.\n"

def check_hyperfind():
    """
    Checks if the selected text matches 'HYPERFIND'.
    Returns True if it matches, False otherwise.
    """
    time.sleep(0.5)
    pyautogui.click(1021, 187)
    time.sleep(0.25)
    pyautogui.click(1021, 187)
    time.sleep(0.25)
    pyautogui.hotkey('ctrl', 'c')  # Copy the selected text to clipboard
    time.sleep(0.1)  # Wait for the clipboard to update
    copied_text = pyperclip.paste()  # Get the text from clipboard
    return copied_text.strip() == 'HYPERFINDS'

def read_and_process_hyperfinds(filename="C:/Users/omalomo3/Desktop/Hyperfinds Automation/Hyperfind Creation/Timi.txt", log_path="C:/Users/omalomo3/Desktop/Hyperfinds Automation/Hyperfind Creation/log.txt"):
    """Reads hyperfind details from a file and processes each entry."""
    with open(filename, "r") as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split(",")
            hyperfind_name, description, cost_centers, orgunit, employment_status, schedule_group = parts

            log_message = process_hyperfind(hyperfind_name, description, cost_centers, orgunit, employment_status, schedule_group)
        
            # Log the processed hyperfind name and success message
            with open(log_path, "a") as log_file:
                log_file.write(log_message)
            if check_hyperfind():
                print(hyperfind_name, "Processed")
            else:
                print("Terminating program.")
                sys.exit()  # Kill the program if the condition is not met
            


read_and_process_hyperfinds()