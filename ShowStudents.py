import pickle

from customtkinter import *


def showDatabase():
    set_appearance_mode('dark')
    set_default_color_theme('dark-blue')

    root = CTk()
    root.resizable(False, False)
    root.title("Show database".title())
    root.geometry("1500x1000")

    frame = CTkFrame(root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # The main lable
    searchLable = CTkLabel(frame, text="show database".upper(), text_font=("Dyuthi", 35))
    searchLable.pack(pady=40, padx=30)

    # The new Framer
    showFrame = CTkFrame(frame)
    showFrame.pack(pady=20, padx=20, fill="both", expand=True)

    try:
        with open('dataFile.dat', 'rb') as dataFile:
            while True:
                rec = StringVar()
                rec = pickle.load(dataFile)
                CTkLabel(showFrame, text=rec, text_font=("Dyuthi", 18)).pack(pady=20, padx=20)



    except EOFError:
        print("Either the file dose not exist or the file exist in a different directory.")
    finally:
        print("This is it!")

    root.mainloop()
