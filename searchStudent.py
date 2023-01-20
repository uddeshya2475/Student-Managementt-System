from customtkinter import *
import pickle
from tkinter import messagebox

def studentSearch():
    set_appearance_mode('dark')
    set_default_color_theme('dark-blue')
    root = CTk()
    root.resizable(False, False)
    root.title("search student".title())
    root.geometry("800x900")
    frame = CTkFrame(root)
    frame.pack(pady=20, padx=20, fill='both', expand=True)

    # The main lable
    searchStudentLable = CTkLabel(frame, text='Search Student'.upper(), text_font=('Dyuthi', 37))
    searchStudentLable.pack(pady=30, padx=30)

    # Search by name and roll no
    searchNameLable = CTkLabel(frame, text="Enter name:".title(), text_font=('Dyuthi', 20))
    searchNameLable.place(relx=0.2, rely=0.18, anchor=CENTER)
    searchNameField = CTkEntry(frame, width=600, height=45, text_font=('Dyuthi', 15))
    searchNameField.place(rely=0.23, relx=0.5, anchor=CENTER)
    searchRollLable = CTkLabel(frame, text='enter roll no:'.title(), text_font=('Dyuthi', 20))
    searchRollLable.place(rely=0.3, relx=0.205, anchor=CENTER)
    searchRollField = CTkEntry(frame, width=600, height=45, text_font=('Dyuthi', 15))
    searchRollField.place(rely=0.35, relx=0.5, anchor=CENTER)

    def linearSearch():
        name = searchNameField.get().title()
        rollNo = searchRollField.get()
        try:
            with open('dataFile.dat', 'rb') as data_file:
                while True:
                    rec = StringVar()
                    rec = pickle.load(data_file)
                    if name == rec['Name:']:
                        CTkLabel(searchResultFrame, text="Name:", text_font=("Dyuthi", 20, 'bold')).place(relx=0.15, rely=0.22, anchor=CENTER)
                        searchResultLabelName.config(text=rec["Name:"])
                        CTkLabel(searchResultFrame, text="Class:", text_font=("Dyuthi", 20, 'bold')).place(relx=0.15, rely=0.37, anchor=CENTER)
                        searchResultLabelAadharCard.config(text=rec["Aadhar Card:"])
                        CTkLabel(searchResultFrame, text="Roll No:", text_font=("Dyuthi", 20, 'bold')).place(relx=0.15, rely=0.52, anchor=CENTER)
                        searchResultLabelRollNo.config(text=rec["RollNo:"])
                        CTkLabel(searchResultFrame, text="Address:", text_font=("Dyuthi", 20, 'bold')).place(relx=0.15, rely=0.67, anchor=CENTER)
                        searchResultLabelAddress.config(text=rec["Address:"])
                        CTkLabel(searchResultFrame, text="Aadhar Card:", text_font=("Dyuthi", 20, 'bold')).place(relx=0.15, rely=0.82, anchor=CENTER)
                        searchResultLabelSection.config(text=rec["Section:"])
                        CTkLabel(searchResultFrame, text="Age:", text_font=("Dyuthi", 20, 'bold')).place(relx=0.15, rely=0.95, anchor=CENTER)
                        searchResultLabelAge.config(text=rec["Age:"])

        except Exception:
            print("This is it!")
        finally:
            print("This is it!")

    # Submit Button

    submitButton = CTkButton(frame, text="search".title(), text_font=("Dyuthi", 25), width=100,
                             height=50,
                             command=linearSearch)

    submitButton.place(rely=0.5, relx=0.5, anchor=CENTER)
    searchResultFrame = CTkFrame(frame, width=720, height=370)
    searchResultFrame.place(rely=0.77, relx=0.5, anchor=CENTER)
    # Search Name
    searchResultLabelName = CTkLabel(searchResultFrame, text="Name will be displayed here, if found.",
                                 text_font=("Dyuthi", 24))
    searchResultLabelName.place(relx=0.5, rely=0.22, anchor=CENTER)

    # Search Section
    searchResultLabelSection = CTkLabel(searchResultFrame, text="Section will be displayed here, if found.",
                                    text_font=("Dyuthi", 24))
    searchResultLabelSection.place(relx=0.5, rely=0.37, anchor=CENTER)

    # Search Roll No
    searchResultLabelRollNo = CTkLabel(searchResultFrame, text="Roll No will be displayed here, if found.",
                                    text_font=("Dyuthi", 24))
    searchResultLabelRollNo.place(relx=0.5, rely=0.52, anchor=CENTER)

    # Search Address
    searchResultLabelAddress = CTkLabel(searchResultFrame, text="Address will be displayed here, if found.",
                                    text_font=("Dyuthi", 24))
    searchResultLabelAddress.place(relx=0.5, rely=0.67, anchor=CENTER)

    # Aadhar Card
    searchResultLabelAadharCard = CTkLabel(searchResultFrame, text="Aadhar Card Number will be displayed here, if found.",
                                    text_font=("Dyuthi", 24))
    searchResultLabelAadharCard.place(relx=0.5, rely=0.82, anchor=CENTER)

    # Age
    searchResultLabelAge = CTkLabel(searchResultFrame, text="Age will be displayed here, if found.",
                                           text_font=("Dyuthi", 24))
    searchResultLabelAge.place(relx=0.5, rely=0.95, anchor=CENTER)


    root.mainloop()
