import tkinter as tk
from PIL import Image, ImageTk
import mss

class outline_window:
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

        self.window.bind("<<reload>>", self.reload)
        self.window.bind("<<close>>", self.close)
        self.window.bind("<<edit>>", self.edit_mode)
        self.window.bind("<<display>>", self.display_mode)
        self.window.bind("<B1-Motion>", self.drag_window)

    def adjust_size(self, x, y):
        self.capt_size[0] += x
        self.capt_size[1] += y
        self.window.geometry(f"{self.capt_size[0]}x{self.capt_size[1]}")
        

    def drag_window(self, event):
        self.window.geometry(f"+{int(event.x_root - self.capt_size[0]/2)}+{int(event.y_root - self.capt_size[1]/2)}")

    def reload(self, event):
        self.window.destroy()
        self.__init__()
    def close(self, event):
        self.window.destroy()
    def edit_mode(self, event):
        self.window.overrideredirect(False)
    def display_mode(self, event):
        self.window.overrideredirect(True)
    def send_event(self, evstr):
        self.window.event_generate(evstr)