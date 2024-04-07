import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
import mss
from capture_window import capture_window
import g_vars as g_vars

class display_window:
    def __init__(self, master, parent, capt):
        self.master = master
        self.parent = parent
        self.window = tk.Toplevel(master)
        self.window.geometry("+100+100")
        self.window.overrideredirect(True)
        self.window.attributes("-topmost", True)

        self.text_label = tk.Label(self.window, text="DISPLAY", background="red")

        self.image_label = tk.Label(self.window)
        self.image_label.pack(side="top")

        self.close_button = tk.Button(self.window, text="Close", background="red", command=self.close_window)


        self.window.bind("<<close>>", lambda e: self.close_window())
        self.window.bind("<<edit>>", self.edit_mode)
        self.window.bind("<<display>>", self.display_mode)

        self.window.bind("<Configure>", self.window_resized)
        self.window.bind("<B1-Motion>", self.drag_window)
        self.window.bind("<Button-1>", self.window_clicked)
        self.window.bind("<ButtonRelease-1>", self.window_unclicked)

        self.capt = capt
        self.capt_size = capt["capt_size"]
        self.capt_pos = capt["capt_pos"]

        self.in_edit_mode = False

        self.run()

    def run(self):
        with mss.mss() as sct:
            monitor = {"left": self.capt_pos[0], "top": self.capt_pos[1], "width": self.capt_size[0], "height": self.capt_size[1]}
            raw = sct.grab(monitor)
        img = Image.frombytes('RGB', raw.size, raw.bgra, 'raw', 'BGRX')
        if(self.in_edit_mode):
            enhancer = ImageEnhance.Brightness(img)
            screenshot = ImageTk.PhotoImage(enhancer.enhance(0.5))
        else:
            screenshot = ImageTk.PhotoImage(img)
        self.image_label.configure(image=screenshot)
        self.image_label.image = screenshot
        self.window.after(g_vars.capture_refresh_wait_ms, self.run)

    def window_resized(self, event):
        pass
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



    def close_window(self):
        if(self.in_edit_mode):
            self.edit_window.send_event("<<close>>")
        self.window.destroy()
    def edit_mode(self, event):
        if(not self.in_edit_mode):
            self.edit_window = capture_window(self.master, self.window, self.capt)
            self.in_edit_mode = True
            self.text_label.pack(side="bottom")
            self.close_button.place(relx=1.0, rely=0, anchor="ne")
    def display_mode(self, event):
        if(self.in_edit_mode):
            self.edit_window.send_event("<<close>>")
            self.in_edit_mode = False
            self.text_label.pack_forget()
            self.close_button.place_forget()
    def send_event(self, evstr):
        self.window.event_generate(evstr)