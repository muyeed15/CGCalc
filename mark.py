# modules
import customtkinter
from customtkinter import *
from warning import warning

# mark extractor
def mark(c, u):
    # storage
    data = [[], [], []]
    enc_data = [[], [], []]
    com_data = ["", ""]

    # GUI
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = CTk()
    root.title("CGCalc")
    root.resizable(False, False)

    # fonts
    font=customtkinter.CTkFont(family="Arial", size=20)

    # frame
    frame0 = CTkFrame(root)
    frame0.pack()

    frame1 = CTkFrame(root, width=570, height=100)
    frame1.pack()
    
    # entry
    for i in range(c+1):
        for j in range(3):
            if i == 0:
                lt = ["Course", "Credits", "Marks"]
                l = CTkLabel(frame0, text=lt[j], font=font)
                l.grid(row=i, column=j, padx=10, pady=10)

            else:
                e = CTkEntry(frame0, width=170)
                e.grid(row=i, column=j, padx=10, pady=10)
                data[j].append(e)

    # optional
    l0 = CTkLabel(frame1, text="Current CGPA    (Optional)")
    l0.place(x=11, y=10)

    d0 = CTkLabel(frame1, text=":")
    d0.place(x=180, y=10)

    e0 = CTkEntry(frame1, width=170)
    e0.place(x=200, y=10)

    l1 = CTkLabel(frame1, text="Current Credits (Optional)")
    l1.place(x=11, y=60)

    d1 = CTkLabel(frame1, text=":")
    d1.place(x=180, y=60)

    e1 = CTkEntry(frame1, width=170)
    e1.place(x=200, y=60)

    # button
    def checker():
        for i in range(c):
            for j in range(3):
                if data[j][i].get() == "":
                    return False
        return True
    

    def checker():
        for i in range(c):
            for j in range(3):

                if (data[j][i].get() == ""):
                    return "string"
                
                if j == 1:
                    try:
                        if float(data[j][i].get()) <= 0:
                            return "small"
                    except:
                        return "float"

                if j == 2:
                    try:
                        float(data[j][i].get())
                    except:
                        return "float-mark"
        
        try:
            if e0.get() == "":
                pass

            elif (float(e0.get()) < 0.00 )or (float(e0.get()) > 4.00):
                return "grade"
        except:
            return "float-grade"
        
        try:
            if e1.get() == "":
                pass

            elif float(e1.get()) <= 0:
                return "small-credits"
        except:
            return "float-credits"
        
        return "pass"
    
    def command():
        if checker() == "string":
            ms = "Error: Please fill all the requirements!"
            warning(ms)
            return

        if checker() == "small":
            ms = "Error: Credits must be more than 0!"
            warning(ms)
            return

        if checker() == "float":
            ms = "Error: Credits must be a valid number!"
            warning(ms)
            return
        
        if checker() == "float-mark":
            ms = "Error: Marks must be a valid number!"
            warning(ms)
            return

        if checker() == "grade":
            ms = "Error: Grade must be in range (0.00 --> 4.00)!"
            warning(ms)
            return
        
        if checker() == "float-grade":
            ms = "Error: Grade must be a valid number!"
            warning(ms)
            return
        
        if checker() == "small-credits":
            ms = "Error: Credits must be more than 0!"
            warning(ms)
            return
        
        if checker() == "float-credits":
            ms = "Error: Credits must be a valid number!"
            warning(ms)
            return

        
        for i in range(c):
            for j in range(3):
                enc_data[j].append(data[j][i].get())

        com_data[0] = e0.get()
        com_data[1] = e1.get()

        root.destroy()
    
    b0 = CTkButton(root, text="Calculate", width=170, command=command)
    b0.pack(pady=10)

    root.mainloop()

    return enc_data, com_data[0], com_data[1]

