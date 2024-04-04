import tkinter as tk
from PIL import Image, ImageTk
import mss

class capture_window:
    def __init__(self, master, capt):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.attributes('-alpha', 0.6)
        self.window.attributes("-topmost", True)

        self.capt_pos = capt["capt_pos"]
        self.capt_size = capt["capt_size"]

        self.window.geometry(f"{self.capt_size[0]}x{self.capt_size[1]}+{self.capt_pos[0]}+{self.capt_pos[1]}")
        self.window.overrideredirect(True)

        self.inc_x = tk.Button(self.window, text="+ Width", command=lambda: self.adjust_size(6, 0))
        self.inc_x.pack(side=tk.TOP, anchor='nw')
        self.dec_x = tk.Button(self.window, text="- Width", command=lambda: self.adjust_size(-6, 0))
        self.dec_x.pack(side=tk.TOP, anchor='nw')
        self.inc_y = tk.Button(self.window, text="+ Height", command=lambda: self.adjust_size(0, 6))
        self.inc_y.pack(side=tk.TOP, anchor='nw')
        self.dec_y = tk.Button(self.window, text="- Height", command=lambda: self.adjust_size(0, -6))
        self.dec_y.pack(side=tk.TOP, anchor='nw')

        self.window.bind("<<close>>", self.close)
        
        self.window.bind("<B1-Motion>", self.drag_window)
        self.window.bind("<Button-1>", self.window_clicked)
        self.window.bind("<ButtonRelease-1>", self.window_unclicked)

    def adjust_size(self, x, y):
        self.capt_size[0] += x
        self.capt_size[1] += y
        self.window.geometry(f"{self.capt_size[0]}x{self.capt_size[1]}")
        

    def window_clicked(self, event):
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

    def close(self, event):
        self.window.destroy()

    def send_event(self, evstr):
        self.window.event_generate(evstr)