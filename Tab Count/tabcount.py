import pyautogui
from tkinter import Tk, Label, Button, LabelFrame, Entry
from threading import Thread

class GlobalTabCounter:
    def __init__(self, master):
        self.master = master
        self.required_tabs = 0  # Number of Tab presses required
        self.setup_gui()

    def setup_gui(self):
        self.master.title("Tab Automation Tool")
        
        self.required_tabs_label = Label(self.master, text="Enter number of Tab key presses:")
        self.required_tabs_label.pack(pady=(30, 0))
        
        self.required_tabs_entry = Entry(self.master)
        self.required_tabs_entry.pack(pady=(0, 30))
        
        self.start_button = Button(self.master, text="Start", command=self.perform_tab_presses)
        self.start_button.pack(pady=5)

    def perform_tab_presses(self):
        try:
            self.required_tabs = int(self.required_tabs_entry.get())
            initial_x, initial_y = 1290,100  # Set to your specific initial click position
            pyautogui.click(initial_x, initial_y)  # Perform the initial click

            # Simulate the required number of Tab key presses
            for _ in range(self.required_tabs):
                pyautogui.press('tab')
                pyautogui.sleep(0.0000000000000000000001)
                

        except ValueError:
            print("Please enter a valid integer for the number of Tab presses.")

if __name__ == "__main__":
    root = Tk()
    app = GlobalTabCounter(root)
    root.mainloop()
