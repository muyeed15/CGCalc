# modules
import customtkinter
from customtkinter import *
from display import display

# result
def result(data, cgpa, creds, ccgpa, ccreds):
    # GUI
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = CTk()
    root.title("CGCalc")

    screen_width = 378
    screen_height = 438
    sys_width, sys_height = display()

    if sys_width != None and sys_height != None:
        root.geometry(f"{screen_width}x{screen_height}+"
                    f"{int((sys_width - screen_width) / 2)}+{int((sys_height - screen_height) / 2)}")

    else:
        root.geometry(f"{screen_width}x{screen_height}")

    # fonts
    font=customtkinter.CTkFont(family="Arial", size=20)

    # frames
    frame0 = CTkFrame(root)
    frame0.pack()

    sframe0 = CTkFrame(frame0, width=137, height=389)
    sframe0.grid(row=0, column=0)

    sframe1 = CTkFrame(frame0)
    sframe1.grid(row=0, column=1)

    # CGPA
    CTkLabel(sframe0, text="THIS SEMESTER").place(x=10, y=0)
    CTkLabel(sframe0, text=f"CGPA", font=font).place(x=10, y=23)
    CTkLabel(sframe0, text=f": {cgpa}", font=font).place(x=77, y=23)
    CTkLabel(sframe0, text=f"Cerdits", font=font).place(x=10, y=47)
    CTkLabel(sframe0, text=f": {creds}", font=font).place(x=77, y=47)

    # Avg CGPA
    if ccgpa == "":
        acgpa = ""
    else:
        acgpa = float("{:.2f}".format((cgpa + float(ccgpa))/2))

    if ccreds == "":
        tcreds = ""
    else:
        tcreds = creds + float(ccreds)

    CTkLabel(sframe0, text="TOTAL").place(x=10, y=80)
    CTkLabel(sframe0, text=f"CGPA", font=font).place(x=10, y=103)
    CTkLabel(sframe0, text=f": {acgpa}", font=font).place(x=77, y=103)
    CTkLabel(sframe0, text=f"Cerdits", font=font).place(x=10, y=127)
    CTkLabel(sframe0, text=f": {tcreds}", font=font).place(x=77, y=127)


    # Gradesheet
    for i in range(16):
        for j in range(3):
            if i == 0:
                label = ["Course", "Credits", "Grade"]
                CTkLabel(sframe1, text=label[j]).grid(row=i, column=j)
            else:
                text = CTkEntry(sframe1, width=79, height=10)

                try:
                    text.insert(0, data[j][i-1].upper())
                except:
                    pass
                
                text.configure(state='disabled')
                text.grid(row=i, column=j)

    def command():
        root.destroy()

    butt = CTkButton(root, text="Exit", command=command)
    butt.pack(pady=10)

    root.resizable(False, False)
    root.mainloop()

