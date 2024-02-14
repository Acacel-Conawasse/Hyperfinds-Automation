import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
import time

class MousePositionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Position Tracker")
        
        # Setup the GUI layout
        self.setup_ui()
        
        # Start the thread to update mouse position
        self.update_position_thread = threading.Thread(target=self.update_position, daemon=True)
        self.update_position_thread.start()

    def setup_ui(self):
        # Label for showing instructions
        self.instructions_label = ttk.Label(self.root, text="Current Mouse Position:", font=("Arial", 12))
        self.instructions_label.pack(pady=(10, 5))
        
        # Label for displaying the mouse coordinates
        self.position_label = ttk.Label(self.root, text="", font=("Arial", 12))
        self.position_label.pack(pady=(5, 10))

    def update_position(self):
        while True:
            # Get the current mouse x, y position
            x, y = pyautogui.position()
            
            # Update the label text with current mouse position
            position_text = f"X: {x}, Y: {y}"
            self.position_label.config(text=position_text)
            
            # Update the GUI every 100 milliseconds
            time.sleep(0.1)
            self.root.update_idletasks()

def main():
    root = tk.Tk()
    app = MousePositionGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
