import random
import pygame
import sys
import random
import tkinter as tk
from tkinter import messagebox

# Function to check the selected answer
# def check_answer(selected_choice):
#     correct_answer = "B"  # Correct answer choice (you can change this)
#     if selected_choice == correct_answer:
#         messagebox.showinfo("Result", "Correct Answer!")
#     else:
#         messagebox.showinfo("Result", "Wrong Answer! Try Again.")

# # Create the main window
# root = tk.Tk()
# root.title("Multiple Choice Question")

# # Create a label for the question
# question_label = tk.Label(root, text="Jess claims Beatrice ate her homework, Beatrice swears thats not the case... There are paper scraps on Beatrice's Desk", font=("Arial", 16))
# question_label.pack(pady=20)

# # Create the four choice buttons
# button_A = tk.Button(root, text="A. Dismiss the claim as absurd without investigating.", font=("Arial", 14), command=lambda: check_answer("A"))
# button_A.pack(pady=5)

# button_B = tk.Button(root, text="B. Ask the class if anyone witnessed what happened.", font=("Arial", 14), command=lambda: check_answer("B"))
# button_B.pack(pady=5)

# button_C = tk.Button(root, text="C. Call Beatrices parents immediatly", font=("Arial", 14), command=lambda: check_answer("C"))
# button_C.pack(pady=5)

# button_D = tk.Button(root, text="D. Give jess new homework", font=("Arial", 14), command=lambda: check_answer("D"))
# button_D.pack(pady=5)

# # Start the GUI main loop
# root.mainloop()

runs1 = random.randint(1, 10)

def popscene1(runs1):
    #if it hasnt already run before
    if runs1== 1:
        print("Jess claims Beatrice ate her homework, Beatrice swears thats not the case... There are paper scraps on Beatrice's Desk")
        opt_A = "A. Dismiss the claim as absurd without investigating."

        opt_B = "B. Ask the class if anyone witnessed what happened.", 

        opt_C = "C. Call Beatrices parents immediatly"

        opt_D = "D. Give jess new homework"

    elif runs1== 2:
        print("Jess claims Beatrice ate her homework, Beatrice swears thats not the case... Jess has previously claimed that her dog ate her homework")
        opt_A = "A. Dismiss the claim as absurd without investigating."

        opt_B = "B. Ask the class if anyone witnessed what happened.", 

        opt_C = "C. Call Beatrices parents immediatly"

        opt_D = "D. Give jess new homework"
    elif runs1== 3:
        print("Pen thief alert! Mark has been caught with two of his classmates' favorite pens. He claims he was just holding them for safekeeping.")
        opt_A = ""

        opt_B = "" 

        opt_C = ""

        opt_D = ""
    elif runs1== 4:
        print("Alex and Mia are playing ‘doctor’ during recess. Mia is now diagnosing kids with homework flu and prescribing no homework for a week.")
        opt_A = ""

        opt_B = "" 

        opt_C = ""

        opt_D = ""
    elif runs1== 5:
        print("")
        opt_A = ""

        opt_B = "" 

        opt_C = ""

        opt_D = ""
    elif runs1== 6:
        print("")
        opt_A = ""

        opt_B = "" 

        opt_C = ""

        opt_D = ""
    elif runs1== 7:
        print("")
        opt_A = ""

        opt_B = "" 

        opt_C = ""

        opt_D = ""
    elif runs1== 8:
        print("")
        opt_A = ""

        opt_B = "" 

        opt_C = ""

        opt_D = ""
    else:
        pass
    

    "Jess claims Beatrice ate her homework"


popup={}
table={}