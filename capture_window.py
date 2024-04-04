import tkinter as tk
from PIL import Image, ImageTk
import mss

class capt_window:
    def __init__(self, master, capt):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.geometry("+50+50")
        self.window.overrideredirect(True)
        self.window.attributes("-topmost", True)

        self.label = tk.Label(self.window)
        self.label.pack()

        self.window.bind("<<reload>>", self.reload)
        self.window.bind("<<close>>", self.close)
        self.window.bind("<<edit>>", self.edit_mode)
        self.window.bind("<<display>>", self.display_mode)
        self.window.bind("<B1-Motion>", self.drag_window)

        self.capt_pos = capt["capt_pos"]
        self.capt_size = capt["capt_size"]

        self.run()

    def run(self):
        with mss.mss() as sct:
            monitor = {"left": self.capt_pos[0], "top": self.capt_pos[1], "width": self.capt_size[0], "height": self.capt_size[1]}
            raw = sct.grab(monitor)
        screenshot = ImageTk.PhotoImage(Image.frombytes('RGB', raw.size, raw.bgra, 'raw', 'BGRX'))
        self.label.configure(image=screenshot)
        self.label.image = screenshot
        self.window.after(50, self.run)

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