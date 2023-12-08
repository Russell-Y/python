#RussellYuan1.py
from PyQt6 import *
import tkinter as tk
from tkinter import *
from gui import *
import csv
from PyQt6.QtWidgets import *



class Menu:
    def __init__(self):
        self.main = main
        
    def vote_menu(self):
        button1 = tk.Button(master=window, text="1: Cameron")
        button2 = tk.Button(text="2: Allison")
        button3 = tk.Button(text="3: Diego")
        exit_button = tk.Button(text="x: Exit")
        vote_button = tk.Button(text="v: Vote")
        
        print('----------------------------------')
        print('VOTE MENU')
        print('----------------------------------')
        print('v: Vote')
        print('x: Exit')
        option = input("Option: ")
        while option != 'x' and option != 'X':
            if option == 'x' or option == 'X':
                break
            if option != 'x' or option != 'X': 
                print('Invalid (v/x): ' + option)
                break
        while option != 'v' and option != 'V': 
            if option == 'v' or option == 'V':
                break
            if option != 'v' or option != 'V': 
                print('Invalid (v/x): ' + option)
                break
        return option


    def candidate_menu(self):
        print('----------------------------------')
        print('CANDIDATE MENU')
        print('----------------------------------')
        print('1: Cameron')
        print('2: Allison')
        print('3: Diego')
        vote = input("Candidate: ")
        while vote > 3 or vote <= 0: 
            if vote == 1:
                print('Voted Cameron')
                break
            elif vote == 2:
                print('Voted Allison')
                break
            elif vote == 3:
                print('Voted Diego')
                break
            elif vote > 3 or vote <= 0:
                print('Invalid (1/2/3): ' + vote)
                break
        return vote
   # main.mainloop()

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