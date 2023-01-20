from customtkinter import *
import sys
from AddStudent import addStudent
from ShowStudents import showDatabase
from searchStudent import studentSearch
from ShowInfo import showInfo
from UpdateStudent import updateStudent
from DelStudent import delStudent


def main():
    set_appearance_mode("Dark")
    set_default_color_theme("dark-blue")

    root = CTk()
    root.resizable(False, False)
    root.title("Student Management System")

    root.geometry("800x900")
    frame = CTkFrame(master=root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    Lable = CTkLabel(master=frame, text="student management system".upper(), text_font=("Dyuthi", 35))
    Lable.pack(pady=40, padx=30)

    # Add student Button
    setButton = CTkButton(master=frame, text="Add Student",
                          text_font=("Dyuthi", 34),
                          corner_radius=10,
                          width=300, height=65,
                          command=addStudent
                          )
    setButton.config(height=300, width=300)
    setButton.pack(pady=20, padx=50)

    # Search Student Button
    SEARCHButton = CTkButton(master=frame, text="Search Student", text_font=("Dyuthi", 34), width=300,
                             command=studentSearch,
                             height=65)
    SEARCHButton.pack(pady=17)

    # Show Database
    SHOWDATABASEButton = CTkButton(master=frame, text="Show Database",
                                   command=showDatabase,
                                   text_font=("Dyuthi", 34), width=300, height=65)
    SHOWDATABASEButton.pack(pady=20)

    updateButton = CTkButton(frame, height=60, width=300, text='Update Student', text_font=("Dyuthi", 34),
                             command=updateStudent)
    updateButton.pack(pady=20, padx=20)
    delButton = CTkButton(frame, height=60, width=300, text='Delete Student', text_font=("Dyuthi", 34),
                          command=delStudent)
    delButton.pack(pady=20, padx=20)

    InfoButton = CTkButton(frame, width=300, height=65, text="Show Info", text_font=("Dyuthi", 34), command=showInfo)
    InfoButton.pack(pady=20)
    # Exit Button
    EXITButton = CTkButton(master=frame, text="Exit", text_font=('Dyuthi', 34), width=300, height=65,
                           fg_color="#FF0000",
                           command=lambda: sys.exit(),
                           hover_color="#F08080",
                           text_color="white"
                           )
    EXITButton.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
