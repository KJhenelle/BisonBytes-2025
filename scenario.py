import random

import tkinter as tk
from tkinter import messagebox

# Function to check the selected answer
def check_answer(selected_choice):
    correct_answer = "B"  # Correct answer choice (you can change this)
    if selected_choice == correct_answer:
        messagebox.showinfo("Result", "Correct Answer!")
    else:
        messagebox.showinfo("Result", "Wrong Answer! Try Again.")

# Create the main window
root = tk.Tk()
root.title("Multiple Choice Question")

# Create a label for the question
question_label = tk.Label(root, text="What is the capital of France?", font=("Arial", 16))
question_label.pack(pady=20)

# Create the four choice buttons
button_A = tk.Button(root, text="A. London", font=("Arial", 14), command=lambda: check_answer("A"))
button_A.pack(pady=5)

button_B = tk.Button(root, text="B. Paris", font=("Arial", 14), command=lambda: check_answer("B"))
button_B.pack(pady=5)

button_C = tk.Button(root, text="C. Berlin", font=("Arial", 14), command=lambda: check_answer("C"))
button_C.pack(pady=5)

button_D = tk.Button(root, text="D. Madrid", font=("Arial", 14), command=lambda: check_answer("D"))
button_D.pack(pady=5)

# Start the GUI main loop
root.mainloop()



def popscene1(runs1):
    #if it hasnt already run before
    if runs1==False:
        opt1=print("Jess claims Beatrice ate her homework, Beatrice swears thats not the case... There are paper scraps on Beatrice's Desk")
        opt0=print("Jess claims Beatrice ate her homework, Beatrice swears thats not the case... Jess has previously claimed that her dog ate her homework")
        


        choice1=input("")

        return runs1=True , 
    else:
        pass
    #"Jess claims Beatrice ate her homework"


popup={}
table={}