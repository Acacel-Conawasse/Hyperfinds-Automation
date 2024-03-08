import pyautogui
import time
import logging
##Script starts from the Hyperfinds Main Screen 
# Setup logging to keep track of actions
logging.basicConfig(filename="log.txt", level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
pyautogui.FAILSAFE = True  # Enable failsafe by moving the mouse to the upper left corner

INITIAL_X, INITIAL_Y = 1290, 100
ADD_DESCRIPTION_X, ADD_DESCRIPTION_Y = 1030,222
SELECT_PLC_X, SELECT_PLC_Y = 1350,455

def move_and_click(x, y, clicks=1, button='left'):
    """Moves the mouse to a specified location and performs a click."""
    pyautogui.moveTo(x, y)
    pyautogui.click(clicks=clicks, button=button)
    time.sleep(0.02)  # Adjusted to the actual wait time
    logging.info(f"Mouse moved and clicked at ({x}, {y}), with a 0.20 second interval")

def mouse_click(x, y):
    pyautogui.click(x, y)
    
def enter_text(text):
    """Enters text at the current cursor location."""
    pyautogui.write(text, interval=0.01)
    logging.info(f"Entered text: {text}")

def tabto(count,INITIAL_X=1290, INITIAL_Y=100):
    mouse_click(INITIAL_X, INITIAL_Y)
    pyautogui.press('tab', presses=count, interval=0.07)

#def tab_and_enter(count):
#    tabto(count)
#    pyautogui.press('enter')
#    time.sleep(1)
    
        
def start_hyperfind_creation():
    """Starts the creation of a new Hyperfind."""
    tabto(3)
    pyautogui.press('enter')
    time.sleep(0.5)
    tabto(3)
    pyautogui.press('left')
    time.sleep(0.5)

def enter_hyperfind_details(hyperfind_name, description):
    """Enters Hyperfind name and description."""
    tabto(2)
    enter_text(hyperfind_name)
    time.sleep(1)
    mouse_click(ADD_DESCRIPTION_X, ADD_DESCRIPTION_Y)
    mouse_click(ADD_DESCRIPTION_X, ADD_DESCRIPTION_Y)
    enter_text(description)
    time.sleep(1)

def add_hyperfind_condition():
    """Navigates to add a new condition for the Hyperfind."""
    tabto(7)
    pyautogui.press('enter')
    time.sleep(1)

def select_primary_labor_category():
    """Selects the primary labor category."""
    tabto(7)
    pyautogui.press('enter')
    time.sleep(1)


def select_and_add_plc_items(plc_type, plc_items):
    """Selects a PLC type and adds items to it."""
    if plc_type == "OrgUnit":
       tabto(37)
       pyautogui.press('enter') 
       time.sleep(2)
       pyautogui.press('tab', presses=3, interval=0.07)
    elif plc_type == "CostCenter":
       tabto(38)
       pyautogui.press('enter') 
       time.sleep(2)
       pyautogui.press('tab', presses=2, interval=0.07)     

    add_plc_items(plc_items)
    pyautogui.press('tab', presses=4, interval=0.07)
    pyautogui.press('enter') 
    time.sleep(0.05)
    tabto(3)
    pyautogui.press('enter')

def add_plc_items(plc_items):
    """Adds items to the selected PLC type."""
    for item in plc_items:
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.05)
        pyautogui.press('backspace')
        enter_text(item.strip())
        pyautogui.press('tab', presses=2, interval=0.07)
        pyautogui.press('enter') 
        time.sleep(0.05)
        pyautogui.hotkey('shift', 'tab')
       
def employment_status_steps():
    """Performs additional steps if employment status is 'Y'."""
    tabto(3)
    pyautogui.press('enter')
    time.sleep(0.05)
    tabto(6)
    pyautogui.press('enter')
    pyautogui.press('tab', presses=26, interval=0.07)
    pyautogui.press('enter')
    time.sleep(0.2)
    tabto(4)
    pyautogui.press('enter')
    time.sleep(0.2)

def schedule_group_steps(schedule_group_text):
    """Performs additional steps if Schedule Group is not 'Null'."""
    if schedule_group_text != "Null":
        tabto(7)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('tab', presses=16, interval=0.07)
        # Enter Schedule group keystrokes
        enter_text(schedule_group_text)
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('tab', presses=2, interval=0.07)
        pyautogui.press('enter')
        pyautogui.press('tab', presses=4, interval=0.07)
        pyautogui.press('enter')
        

def finalize_hyperfind_creation():
    """Finalizes and saves the Hyperfind."""
    pyautogui.press('tab', presses=2, interval=0.07)
    pyautogui.press('enter')
    time.sleep(3)
    tabto(7)
    pyautogui.press('enter')
    time.sleep(3)

def process_hyperfind(hyperfind_name, description, cost_centers, orgunit, employment_status, schedule_group):
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

    finalize_hyperfind_creation()

def read_and_process_hyperfinds(filename="C:/Users/mdees1/Desktop/Hyperfinds-Automation/Hyperfind Creation/Matt-Hyperfinds.txt"):
    """Reads hyperfind details from a file and processes each entry."""
    with open(filename, "r") as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split(",")
            hyperfind_name, description, cost_centers, orgunit, employment_status, schedule_group = parts

            process_hyperfind(hyperfind_name, description, cost_centers, orgunit, employment_status, schedule_group)

# Start the process
read_and_process_hyperfinds()
