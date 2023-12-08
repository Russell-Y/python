from PyQt6 import *
from gui import *
import csv
import tkinter as tk
from tkinter import *
from PyQt6.QtWidgets import *


class Classroom:
    def __init__(self):
        button_1 = tk.Button(master=window, text="1: Cameron")
        button_2 = tk.Button(text="2: Allison")
        button_3 = tk.Button(text="3: Diego")
        exit_button = tk.Button(text="x: Exit")
        vote_button = tk.Button(text="v: Vote")
        
    def stats(self): 
        students = int(input("Total number of students: "))
        scores = list(map(int, input(f'Enter {students} score(s): ').split()))


        student = 0
        score = 0
        mean = 0
        grades = ''
        grade = ''
    def scorekeeping(self): 
        if scores[student] != students or scores[student] < students:
            scores = list(map(int, input(f'Enter {students} score(s): ').split()))
        elif scores[student] > students:
            scores.pop(-1)

    def grades(self): 
        for student in range(students):
            student += 1
            mean = sum(scores[0:]) / students
            if scores[student - 1] >= 70:
                grades = 'A'
            elif scores[student - 1] >= 50 and scores[student - 1] <= 70:
                grades = 'B'
            elif scores[student - 1] >= 40 and scores[student - 1] <= 50:
                grades = 'C'
            elif scores[student - 1] >= 30 and scores[student - 1] <= 40:
                grades = 'D'
            elif scores[student - 1] < 30:
                grades = 'F'
            print(f'Student {student} score is {scores[student - 1]} and grade is {grades}')
            
           # for item in scores:
            #    scores = item
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
