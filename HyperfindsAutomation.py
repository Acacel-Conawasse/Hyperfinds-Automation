import pyautogui
import time
import logging

# Setup logging to keep track of actions
logging.basicConfig(filename="log.txt", level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def move_and_click(x, y, clicks=1, button='left'):
    """Moves the mouse to a specified location and performs a click."""
    pyautogui.moveTo(x, y)
    pyautogui.click(clicks=clicks, button=button)
    time.sleep(0.02)  # Adjusted to the actual wait time
    logging.info(f"Mouse moved and clicked at ({x}, {y}), with a 0.20 second interval")

def enter_text(text):
    """Enters text at the current cursor location."""
    pyautogui.write(text, interval=0.02)
    logging.info(f"Entered text: {text}")

def start_hyperfind_creation():
    """Starts the creation of a new Hyperfind."""
    move_and_click(1009, 263)
    time.sleep(0.5)
    move_and_click(1334, 258)
    time.sleep(0.5)
    move_and_click(1334, 258)
    time.sleep(0.5)

def enter_hyperfind_details(hyperfind_name, description):
    """Enters Hyperfind name and description."""
    move_and_click(1100, 221)
    time.sleep(0.72)
    enter_text(hyperfind_name)
    move_and_click(1039, 252)
    time.sleep(0.72)
    move_and_click(1040, 253)
    enter_text(description)

def add_hyperfind_condition():
    """Navigates to add a new condition for the Hyperfind."""
    move_and_click(1442, 503)
    time.sleep(2.7)

def select_primary_labor_category():
    """Selects the primary labor category."""
    move_and_click(1095, 408)
    time.sleep(2.7)

def select_and_add_plc_items(plc_type, plc_items):
    """Selects a PLC type and adds items to it."""
    plc_coordinates = {
        "CostCenter": (1322, 316),
        "OrgUnit": (1764, 283),
    }
    x, y = plc_coordinates[plc_type]
    move_and_click(x, y)
    time.sleep(0.20)  # Wait for the selection to take effect

    add_plc_items(plc_items)

def add_plc_items(plc_items):
    """Adds items to the selected PLC type."""
    for item in plc_items:
        move_and_click(1427, 446)
        time.sleep(0.72)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.72)
        pyautogui.press('backspace')
        enter_text(item.strip())
        move_and_click(1456, 475)
        time.sleep(0.72)
        move_and_click(1584, 478)
        time.sleep(1)

def employment_status_steps():
    """Performs additional steps if employment status is 'Y'."""
    move_and_click(1431, 776)
    time.sleep(0.72)
    move_and_click(1077, 662)
    time.sleep(0.72)
    move_and_click(1147, 381)
    time.sleep(0.72)
    #move_and_click(1419, 789)
    #time.sleep(0.72)

def finalize_hyperfind_creation():
    """Finalizes and saves the Hyperfind."""
    move_and_click(1417, 777)
    time.sleep(3)
    move_and_click(1856, 996)
    time.sleep(3.2)
    move_and_click(1796, 994)
    time.sleep(3)

def process_hyperfind(hyperfind_name, description, cost_centers, orgunit, employment_status):
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

    finalize_hyperfind_creation()

def read_and_process_hyperfinds(filename="hytest.txt"):
    """Reads hyperfind details from a file and processes each entry."""
    with open(filename, "r") as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split(",")
            hyperfind_name, description, cost_centers, orgunit, employment_status = parts

            process_hyperfind(hyperfind_name, description, cost_centers, orgunit, employment_status)

# Start the process
read_and_process_hyperfinds()
