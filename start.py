# modules
import customtkinter
from customtkinter import *
from warning import warning
from database import uni_list
from display import display

# start
def start():
    # storage
    data = [None, None, None]

    # GUI
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = CTk()
    root.title("CGCalc")

    screen_width = 350
    screen_height = 170
    sys_width, sys_height = display()

    if sys_width != None and sys_height != None:
        root.geometry(f"{screen_width}x{screen_height}+"
                    f"{int((sys_width - screen_width) / 2)}+{int((sys_height - screen_height) / 2)}")
    
    else:
        root.geometry(f"{screen_width}x{screen_height}")

    root.resizable(False, False)

    # fonts
    font=customtkinter.CTkFont(family="Arial", size=20)

    # course
    l0 = CTkLabel(root, text="Number of Courses", font=font)
    l0.place(x=10, y=10)

    d0 = CTkLabel(root, text=":", font=font)
    d0.place(x=186, y=10)

    e0 = CTkEntry(root)
    e0.place(x=200, y=10)

    # method
    l1 = CTkLabel(root, text="Method", font=font)
    l1.place(x=10, y=50)

    d1 = CTkLabel(root, text=":", font=font)
    d1.place(x=186, y=50)

    opm = ["Select", "Grade", "Mark"]

    o0 = CTkOptionMenu(root, values=opm)
    o0.place(x=200, y=50)

    # university
    l2 = CTkLabel(root, text="University", font=font)
    l2.place(x=10, y=90)

    o1 = CTkOptionMenu(root, values=uni_list())
    o1.place(x=200, y=90)

    d2 = CTkLabel(root, text=":", font=font)
    d2.place(x=186, y=90)

    # next
    def command():
        try:
            if (0 < float(e0.get()) < 16) and (e0.get() != "") and (o0.get() != "Select") and (o1.get() != "Select"):
                data[0] = e0.get()
                data[1] = o0.get()
                data[2] = o1.get()
                root.destroy()
            
            elif (0 > float(e0.get())) or (float(e0.get()) > 16):
                ms = "Error: Number of course must be a valid number! (1-15)"
                warning(ms)
            
            else:
                ms = "Error: Please fill all the requirements!"
                warning(ms)
                
        except:
                ms = "Error: Number of course must be a valid number! (1-15)"
                warning(ms)


    b0 = CTkButton(root, text="Next", command=command)
    b0.place(x=107, y=130)

    root.mainloop()

    return data[0], data[1], data[2]

