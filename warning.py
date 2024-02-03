# modules
import customtkinter
from customtkinter import *
from display import display

# warning
def warning(ms):
    # GUI
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = CTk()
    root.title("Warning")

    screen_width = 350
    screen_height = 170
    sys_width, sys_height = display()

    if sys_width != None and sys_height != None:
        root.geometry(f"{screen_width}x{screen_height}+"
                    f"{int((sys_width - screen_width) / 2)}+{int((sys_height - screen_height) / 2)}")
    
    else:
        root.geometry(f"{screen_width}x{screen_height}")

    CTkLabel(root, text="\n"*3 + ms + "\n"*3).pack()

    # button
    def command():
        root.destroy()
    
    CTkButton(root, text="Okay", command=command).pack()

    root.resizable(False, False)
    root.mainloop()

