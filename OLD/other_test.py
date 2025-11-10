import tkinter as tk
from time import sleep


class CustomCanvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.last_click_event = None  # Initialize with None to indicate no clicks yet
        self.bind("<Button-1>", self.record_click)  # Bind left mouse click

    def record_click(self, event):
        """Handler function to record the position of a mouse click."""
        self.last_click_event = event  # Store the entire event

    def get_last_mouse_click(self):
        """Return the position of the last mouse click or None if no clicks."""
        if self.last_click_event is not None:
            return [self.last_click_event.x, self.last_click_event.y]
        else:
            return None


# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    canvas = CustomCanvas(root, width=400, height=400)
    canvas.pack()
    # After closing the Tkinter window, you can get the last click position
    while True:
        print(canvas.get_last_mouse_click())
        sleep(0.5)
        root.update()
    # root.mainloop()
