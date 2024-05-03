import pyautogui
import pyperclip
import time

def final_validation_step():
    # Click to focus and select the item, and copy it to the clipboard
    #pyautogui.click(1194, 318)
    #pyautogui.hotkey('ctrl', 'c')
    #time.sleep(0.1)  # Wait a bit for the clipboard to update

    # Retrieve and process the copied text
    copied_text = "Primary labor category matches */*/*/*/*/4500220003, 4500220004, 4500220006, 4500220007, 4500220005 as of today"
    copied_numbers = set(''.join(filter(str.isdigit, copied_text)).split(','))

    # Define and process the plc_items
    plc_items = "4500220003#4500220004#4500220006#4500220007#4500220005"
    plc_numbers = set(''.join(filter(str.isdigit, plc_items)).split('#'))

    # Compare the two sets of numbers
    if copied_numbers == plc_numbers:
        return "All items match."
    else:
        # Log the unmatched items
        with open("unsure_costcenters.txt", "a") as file:
            file.write("Unmatched items found. First element: {}\n".format(next(iter(copied_numbers))))
        print("col[0] not created")
        #pyautogui.click(1711, 993)  # Perform the error click
        return "Items do not match."

# Run the validation
result = final_validation_step()
print(result)
