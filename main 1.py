#from RussellYuan1.py.py import *
from RussellYuan1.py import *
#from RussellYuan1 import *
from PyQt6 import *
import tkinter as tk
from tkinter import *
from gui import *
import csv
from PyQt6.QtWidgets import *



def main():
    window = tk.Tk()
    window.title("VOTE MENU")
    button_1 = tk.Button(master=window, text="1: Cameron")
    button_2 = tk.Button(text="2: Allison")
    button_3 = tk.Button(text="3: Diego")
    exit_button = tk.Button(text="x: Exit")
    vote_button = tk.Button(text="v: Vote")
    
    window.geometry('300x200')
    window.resizable(True, True)
    Gui(window)
    window.mainloop()
        
        
    application = QApplication([])
    window.setGeometry(0, 0, 300, 100)
    window.show()
    application.exec()
    window.mainloop()
    print('----------------------------------')
    print(f'Cameron - 1, Allison - 2, Diego - 1, Total - 4')
    print('----------------------------------')
    option = ''
    vote = 0
    while option != 'x' or option != 'X':
        vote_menu()
        if option == 'v' or option == 'V':
            candidate_menu()
        break



if __name__ == '__main__':
    main()
