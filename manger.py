import tkinter as tk
from capture_window import capt_window
from outline_window import outline_window

root = tk.Tk()
root.title("GuiAnywhere")
root.attributes("-topmost", True)

capt_windows = []
def send_event_all(evstr):
    for window in capt_windows:
        window.send_event(evstr)

def bigger_x():
    capt_windows[0].capt_size[0]+=1
def bigger_y():
    capt_windows[0].capt_size[1]+=1
edit_button = tk.Button(root, text="bigger_x", command=lambda: bigger_x())
edit_button.pack()
display_button = tk.Button(root, text="bigger_y", command=lambda: bigger_y())
display_button.pack()


capts = []
capts.append({"capt_pos":[-500, 30], "capt_size":[300, 300]})
capts.append({"capt_pos":[100, 100], "capt_size":[200, 200]})

lebel = tk.Label(root, text="HELLO")
lebel.pack()

o = outline_window(root, capts[0])
capt_windows.append(capt_window(root, capts[0]))
#capt_windows.append(cpt_window(root, capts[1]))
root.mainloop()