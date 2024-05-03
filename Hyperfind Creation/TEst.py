import pyautogui
import pyperclip
import time

def final_validation_step(hyperfind_name,cost_centers,orgunit):
    # Click to focus and select the item, and copy it to the clipboard
    #pyautogui.click(1194, 318)
    #pyautogui.hotkey('ctrl', 'c')
    #time.sleep(0.1)  # Wait a bit for the clipboard to update

    # Retrieve and process the copied text
    copied_text = "Primary labor category matches */*/*/*/*/4500220003, 4500220004, 4500220006, 4500220007, 4500220005 as of today"
    copied_numbers = set(''.join(filter(str.isdigit, copied_text)).split(','))

    # Define and process the plc_items

    

        # Retrieve and process the copied text
    copied_text = pyperclip.paste()
    copied_numbers = set(''.join(filter(str.isdigit, copied_text)).split(','))
    if cost_centers != "Null":
        expetedConditions = set(''.join(filter(str.isdigit, cost_centers)).split('#'))
    if orgunit !="Null":
        expetedConditions = set(''.join(filter(str.isdigit,orgunit)).split('#'))
        
    
    # Compare the two sets of numbers
    if copied_numbers == expetedConditions:
        print ("All items match.")
    else:
        # Log the unmatched items
        with open("unsure_costcenters.txt", "a") as file:
            file.write("\n"+"Unmatched items found. First element: {}\n".format(next(iter(copied_numbers))))
            file.write(hyperfind_name +" not created"+ "\n")
            file.write("-----------------------------------------------------------------")
        print(hyperfind_name +"not created")

# Run the validation
result = final_validation_step()
print(result)
