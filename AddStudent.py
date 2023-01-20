import pickle

from customtkinter import *
from tkinter import messagebox
import time



def addStudent():
    set_appearance_mode("Dark")
    set_default_color_theme("dark-blue")
    rootWin = CTk()
    rootWin.resizable(False, False)
    rootWin.title("add student".title())
    rootWin.geometry("800x1000")
    frame = CTkFrame(master=rootWin)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Lable
    addStudentLable = CTkLabel(frame, text="Add student".upper(), text_font=("Dyuthi", 37))
    addStudentLable.pack(pady=30, padx=30)

    # The name field
    nameLable = CTkLabel(frame, text="Enter name here: ".upper(), text_font=('Dyuthi', 20))
    nameLable.place(relx=0.25, rely=0.15, anchor=CENTER)
    nameField = CTkEntry(frame, width=600, height=50, text_font=('Dyuthi', 15))
    nameField.place(relx=0.5, rely=0.22, anchor=CENTER)

    ageLable = CTkLabel(frame, text="Enter age:".upper(), text_font=('Dyuthi', 20))
    # The class and age field
    ageLable.place(relx=0.189, rely=0.3, anchor=CENTER)
    ageField = CTkEntry(frame, width=60, height=50, text_font=('Dyuthi', 15))
    ageField.place(relx=0.35, rely=0.3, anchor=CENTER)
    classLable = CTkLabel(frame, text="Enter class:".upper(), text_font=("Dyuthi", 20))
    classLable.place(relx=0.68, rely=0.3, anchor=CENTER)
    classField = CTkEntry(frame, width=60, height=50, text_font=('Dyuthi', 15))
    classField.place(relx=0.86, rely=0.3, anchor=CENTER)

    # The Roll Number field
    rollLable = CTkLabel(frame, text="roll number:".upper(), text_font=("Dyuthi", 20))
    rollLable.place(relx=0.21, rely=0.39, anchor=CENTER)
    rollField = CTkEntry(frame, width=600, height=50, text_font=('Dyuthi', 15))
    rollField.place(relx=0.5, rely=0.45, anchor=CENTER)

    # The Address field
    addressLable = CTkLabel(frame, text="address:".upper(), text_font=("Dyuthi", 20))
    addressLable.place(rely=0.53, relx=0.18, anchor=CENTER)
    adressField = CTkEntry(frame, width=600, height=50, text_font=('Dyuthi', 15))
    adressField.place(rely=0.6, relx=0.5, anchor=CENTER)

    # The aadhar field
    aadharLable = CTkLabel(frame, text="enter aadhar number:".upper(), text_font=("Dyuthi", 20))
    aadharLable.place(rely=0.72, relx=0.292, anchor=CENTER)
    aadharField = CTkEntry(frame, width=300, height=50, text_font=('Dyuthi', 15))
    aadharField.place(rely=0.72, relx=0.7, anchor=CENTER)

    def validate():
        name = str(nameField.get())
        name.title()
        age = int(ageField.get())
        section = int(classField.get())
        rollNo = int(rollField.get())
        address = adressField.get()
        aadharNumber = aadharField.get()
        if len(aadharNumber) > 12 or len(aadharNumber) < 12:
            messagebox.showerror(title="Aadhar Card Number Error", message="The aadhar number should not be more than "
                                                                           "of less than 12.")
            sys.exit()
        elif len(str(rollNo)) > 4 or len(str(rollNo)) < 4:
            messagebox.showerror(title="Roll Number Error", message="The roll number should be exactly of 4 digits.")
            sys.exit()
        else:
            try:
                with open('dataFile.dat', 'ab') as record_file:
                    finalData = {"Name:": name, "Age:": age, "Section:": section, "RollNo:": rollNo,
                                 "Address:": address, "Aadhar Card:": aadharNumber}
                    pickle.dump(finalData, record_file)

            except EOFError:
                messagebox.showinfo(title="Error of File", message="The datafile dose not exist or it is not in the "
                                                                    "same directory.")
            finally:
                messagebox.showinfo(title="Student Save Status", message="Student saved successfully.")


    # The submit button
    submitButton = CTkButton(frame, text="submit".upper(),
                             width=200, height=65,
                             text_font=("Dyuthi", 35), corner_radius=10,
                             command=validate)
    submitButton.place(rely=0.9, relx=0.5, anchor=CENTER)
    rootWin.mainloop()


if __name__ == "__main__":
    print(addStudent())
