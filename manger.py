import tkinter as tk
from display_window import display_window

root = tk.Tk()
root.title("GuiAnywhere")
root.geometry("200x100")
root.minsize(250, 40)
root.maxsize(250, 40)
root.attributes("-topmost", True)

capt_windows = []
capts = []

def update_windows_list():
    indexs = []
    for i in range(len(capt_windows)):
        if(not capt_windows[i].window.winfo_exists()):
            indexs.insert(0, i)
    for i in indexs:
        capt_windows.pop(i)

def send_event_all(evstr):
    update_windows_list()
    for window in capt_windows:
        window.send_event(evstr)


def change_edit_mode():
    global in_edit_mode
    in_edit_mode = not in_edit_mode
    if(in_edit_mode):
        send_event_all("<<edit>>")
        edit_button.config(background="green")
    else:
        send_event_all("<<display>>")
        edit_button.config(background="grey")     

def new_capture():
    capts.append({"capt_size":[110, 110], "capt_pos":[50, 50]})
    capt_windows.append(display_window(root, root, capts[-1]))
    if(in_edit_mode):
        index = len(capt_windows)-1
        root.after(200, lambda: capt_windows[index].send_event("<<edit>>"))

in_edit_mode = False
edit_button = tk.Button(root, text="Edit Mode", command=change_edit_mode, background="grey")
edit_button.pack(side="left", fill="both", expand=True)


add_button = tk.Button(root, text="Add", command=new_capture, background="grey")
add_button.pack(side="right", fill="both", expand=True)

root.mainloop()