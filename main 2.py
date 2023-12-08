from RussellYuan2.py import *
from RussellYuan2 import *
from PyQt6 import *
import tkinter as tk
from tkinter import *
from gui import *
import csv
from PyQt6.QtWidgets import *


def main():
    window = tk.Tk()
    window.title("Classroom")
    window.geometry('300x200')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()
        
        
    application = QApplication([])
    window.setGeometry(0, 0, 300, 100)
    window.show()
    application.exec()
    window.mainloop()
        
    stats()
    scorekeeping()
    grades()



if __name__ == '__main__':
    main()
    print(f'The average score is {mean:.2f}, a grade of {grades}')
    