import tkinter as tk
from display_window import display_window
from capture_window import capture_window

root = tk.Tk()
root.title("GuiAnywhere")
root.attributes("-topmost", True)

capt_windows = []
def send_event_all(evstr):
    for window in capt_windows:
        window.send_event(evstr)


edit_button = tk.Button(root, text="Start Edit Mode", command=lambda: send_event_all("<<edit>>"))
edit_button.pack()
display_button = tk.Button(root, text="End Edit Mode", command=lambda: send_event_all("<<display>>"))
display_button.pack()



capts = []
capts.append({"capt_pos":[500, 30], "capt_size":[300, 300]})
capts.append({"capt_pos":[100, 100], "capt_size":[200, 200]})

lebel = tk.Label(root, text="HELLO")
lebel.pack()

#o = outline_window(root, capts[0])
capt_windows.append(display_window(root, capts[0]))
capt_windows.append(display_window(root, capts[1]))
root.mainloop()