import pickle

from customtkinter import *
import tkinter
from tkinter import messagebox


def updateStudent():
    set_appearance_mode('dark')
    set_default_color_theme('dark-blue')
    root = CTk()
    root.resizable(False, False)
    root.title("Update Student Info".title())
    root.geometry("800x950")
    frame = CTkFrame(root)
    frame.pack(pady=20, padx=20, fill='both', expand=True)

    # The main lable
    studentSearchText = CTkLabel(frame, text='update student info'.upper(), text_font=('Dyuthi', 37))
    studentSearchText.pack(pady=30, padx=30)

    # Search by name and roll no
    searchNameText = CTkLabel(frame, text="Enter name:".title(), text_font=('Dyuthi', 20))
    searchNameText.place(relx=0.2, rely=0.18, anchor=CENTER)
    searchName = CTkEntry(frame, width=600, height=45, text_font=('Dyuthi', 15))
    searchName.place(rely=0.23, relx=0.5, anchor=CENTER)
    searchRollText = CTkLabel(frame, text='enter roll no:'.title(), text_font=('Dyuthi', 20))
    searchRollText.place(rely=0.3, relx=0.205, anchor=CENTER)
    searchRollNo = CTkEntry(frame, width=600, height=45, text_font=('Dyuthi', 15))
    searchRollNo.place(rely=0.35, relx=0.5, anchor=CENTER)

    frameTwo = CTkFrame(frame, width=720, height=530)
    frameTwo.place(rely=0.7, relx=0.5, anchor=CENTER)

    # The second framer things
    # Name text and field
    newNameText = CTkLabel(frameTwo, text="Enter name:".title(), text_font=("Dyuthi", 20)).place(rely=0.2, relx=0.15,
                                                                                                 anchor=CENTER)
    newName = CTkEntry(frameTwo, text_font=("Dyuthi", 18), width=450, height=50).place(rely=0.2, relx=0.62,
                                                                                       anchor=CENTER)

    # Aadhar Card Text and field
    newAadharText = CTkLabel(frameTwo, text='enter aadhar number:'.title(), text_font=("Dyuthi", 20)).place(
        relx=0.225, rely=0.35, anchor=CENTER
    )
    newAadhar = CTkEntry(frameTwo, text_font=("Dyuthi", 18), width=370, height=50).place(
        relx=0.68, rely=0.35, anchor=CENTER
    )

    # Roll No text and field
    newRollText = CTkLabel(frameTwo, text="Enter roll no:".title(), text_font=("Dyuthi", 20)).place(
        relx=0.16, rely=0.5, anchor=CENTER
    )
    newRoll = CTkEntry(frameTwo, text_font=("Dyuthi", 20), width=435, height=50).place(
        relx=0.64, rely=0.5, anchor=CENTER
    )

    # Age and class text and field
    newAgeText = CTkLabel(frameTwo, text="enter age:".title(), text_font=("Dyuthi", 20)).place(
        relx=0.138, rely=0.66, anchor=CENTER
    )
    newAge = CTkEntry(frameTwo, text_font=("Dyuthi", 20), width=50, height=50).place(
        relx=0.3, rely=0.66, anchor=CENTER
    )
    newClassText = CTkLabel(frameTwo, text='enter class:'.title(), text_font=("Dyuthi", 20)).place(
        relx=0.72, rely=0.66, anchor=CENTER
    )
    newClass = CTkEntry(frameTwo, text_font=("Dyuthi", 20), width=55, height=50).place(
        relx=0.9, rely=0.66, anchor=CENTER
    )

    # The submit button


    def searchStatus():
        oldName = searchName.get()

        try:
            with open("dataFile.dat", 'rb') as binaryFile:
                while True:
                    rec = pickle.load(binaryFile)
                    if rec["Name:"] == oldName:
                        CTkLabel(frameTwo, text="Student Found...", text_font=("Dyuthi", 20)).place(relx=0.75,
                                                                                                    rely=0.77,
                                                                                                    anchor=CENTER)
        except EOFError:
            print("This is it")
        finally:
            print("This is the end of file")

    def buttonUpdate():
        messagebox.showinfo(title="Entry successful...", message="Student update Successful")

    updateButton = CTkButton(frameTwo, text="Update", text_font=("Dyuthi", 30)
                             , height=70, width=300, command=buttonUpdate).place(rely=0.9, relx=0.25, anchor=CENTER)

    checkButton = CTkButton(frameTwo, text="Check Student", text_font=("Dyuthi", 30), height=70, width=300,
                            fg_color='red', hover_color="pink", command=searchStatus).place(
        rely=0.9, relx=0.75, anchor=CENTER
    )

    root.mainloop()
