from customtkinter import *


def showInfo():
    root = CTk()
    frame = CTkFrame(root)
    root.geometry('700x800')
    root.resizable(False, False)
    root.title("Information")
    frame.pack(pady=20, padx=20, fill='both', expand=True)

    projectName = CTkLabel(frame, text_font=("Dyuthi", 25), text="Project Name:")
    projectName.place(relx=0.23, rely=0.1, anchor=CENTER)
    projectNameThing = CTkLabel(frame, text_font=("Dyuthi", 25), text="Student Management System")
    projectNameThing.place(relx=0.55, rely=0.17, anchor=CENTER)

    candidateNames = CTkLabel(frame, text_font=("Dyuthi", 25), text="Candidates:")
    candidateNames.place(relx=0.2, rely=0.25, anchor=CENTER)

    nameONe = CTkLabel(frame, text_font=("Dyuthi", 25), text="Vaishnavi Singh")
    nameONe.place(relx=0.5, rely=0.35, anchor=CENTER)
    nameTwo = CTkLabel(frame, text_font=("Dyuthi", 25), text="Vaibhav Rana")
    nameTwo.place(relx=0.48, rely=0.42, anchor=CENTER)
    nameThree = CTkLabel(frame, text_font=("Dyuthi", 25), text="Uddeshya Singh")
    nameThree.place(relx=0.5, rely=0.49, anchor=CENTER)

    nameMentor = CTkLabel(frame, text_font=("Dyuthi", 25), text="Mentor:")
    nameMentor.place(relx=0.17, rely=0.57, anchor=CENTER)
    mentorName = CTkLabel(frame, text="Ms. Prabhjot Kaur", text_font=("Dyuthi", 25))
    mentorName.place(relx=0.5, rely = 0.66, anchor=CENTER)

    modulesName = CTkLabel(frame, text="Modules used:", text_font=("Dyuthi", 25))
    modulesName.place(relx=0.08, rely=0.75)

    moduleList = CTkLabel(frame, text="Pickle, Tkinter, CustomTkinter, DateTime", text_font=("Dyuthi", 25))
    moduleList.place(relx=0.5, rely=0.88, anchor=CENTER)





    root.mainloop()