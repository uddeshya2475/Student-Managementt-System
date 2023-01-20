import pickle

from customtkinter import *
import tkinter
from tkinter import messagebox


def delStudent():
    root = CTk()
    root.title("Delete Student")
    root.geometry("1000x400")
    frame = CTkFrame(root)
    frame.pack(pady=20, padx=20, fill='both', expand=1)

    mainLabel = CTkLabel(frame, text="Deleter Student".upper(), text_font=("Dyuthi", 32))
    mainLabel.place(relx=0.5, rely=0.1, anchor=CENTER)

    nameLabel = CTkLabel(frame, text='Name:', text_font=("Dyuthi", 22)).place(relx=0.08, rely=0.38, anchor=CENTER)
    nameEnt = CTkEntry(frame, width=550, height=50, text_font=("Dyuthi", 22)).place(relx=0.45, rely=0.38,
                                                                                      anchor=CENTER)

    rollLabel = CTkLabel(frame, text="Roll No:", text_font=("Dyuthi", 22)).place(relx=0.09, rely=0.7, anchor=CENTER)
    rollEntry = CTkEntry(frame, width=550, height=50, text_font=("Dyuthi", 22)).place(relx=0.45, rely=0.7,
                                                                                      anchor=CENTER)

    def linearSearchThing():
        CTkLabel(frame, text="Student Found..", text_font=("Dyuthi", 20)).place(relx=0.86, rely=0.18, anchor=CENTER)
    def delSearch():
        messagebox.showinfo(title="Success", message="Student Removed Successfully.")

    checkButton = CTkButton(frame, width=200, height=60, text="Check", text_font=("Dyuthi", 22), fg_color='red',
                            command=linearSearchThing).place(relx=0.87, rely=0.38, anchor=CENTER)
    delButton = CTkButton(frame, width=200, height=60, text="Delete", text_font=("Dyuthi", 22),
                          command=delSearch).place(relx=0.87,rely=0.7,anchor=CENTER)

    root.mainloop()
