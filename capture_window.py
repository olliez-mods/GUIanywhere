import tkinter as tk
from tkinter import ttk

class capture_window:
    def __init__(self, master, parent, capt):
        self.master = master
        self.parent = parent
        self.window = tk.Toplevel(master)
        self.window.attributes('-alpha', 0.5)
        self.window.attributes("-topmost", True)
        self.window.overrideredirect(True)
        self.window.minsize(50, 50)

        self.capt = capt
        self.capt_pos = capt["capt_pos"]
        self.capt_size = capt["capt_size"]

        self.dragging = False

        self.window.geometry(f"{self.capt_size[0]}x{self.capt_size[1]}+{self.capt_pos[0]}+{self.capt_pos[1]}")

        self.grip = ttk.Sizegrip(self.window)
        self.grip.place(relx=1.0, rely=1.0, anchor="se")

        self.window.bind("<<close>>", self.close)

        self.window.bind("<B1-Motion>", self.drag_window)
        self.window.bind("<Button-1>", self.window_clicked)
        self.window.bind("<ButtonRelease-1>", self.window_unclicked)

    def adjust_size(self, x, y):
        self.capt_size[0] += x
        self.capt_size[1] += y
        self.window.geometry(f"{self.capt_size[0]}x{self.capt_size[1]}")


    def window_clicked(self, event):
        if(event.widget.winfo_class() == "TSizegrip"):
            self.dragging = False
            return
        self.dragging = True
        self.mouse_x = event.x
        self.mouse_y = event.y
            
    def window_unclicked(self, event):
        self.dragging = False
    def drag_window(self, event):
        if self.dragging:
            deltax = event.x - self.mouse_x
            deltay = event.y - self.mouse_y
            x = self.window.winfo_x() + deltax
            y = self.window.winfo_y() + deltay
            self.window.geometry(f"+{x}+{y}")
            self.capt_pos[0], self.capt_pos[1] = x, y
        self.capt_size[0], self.capt_size[1] = self.window.winfo_width(), self.window.winfo_height()


    def close(self, event):
        self.window.destroy()

    def send_event(self, evstr):
        self.window.event_generate(evstr)