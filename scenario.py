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

# runs1 = random.randint(1, 10)

def popscene1(runs1):
    if runs1 == 1:
        scenario = "Jess claims Beatrice ate her homework, Beatrice swears that's not the case... There are paper scraps on Beatrice's Desk."
        options = [
            "A. Dismiss the claim as absurd without investigating.",
            "B. Ask the class if anyone witnessed what happened.",
            "C. Call Beatrice's parents immediately.",
            "D. Give Jess new homework."
        ]
        scores= ["neglectful","okay", "strict", "okay"]
    elif runs1 == 2:
        scenario = "Blake claims Anna ate her homework, Anna swears that's not the case... Blake has previously claimed that his dog ate his homework."
        options = [
            "A. Dismiss the claim as absurd.",
            "B. Scold Blake for lying.",
            "C. Call Anna's parents immediately.",
            "D. Give Blake new homework."
        ]
        scores= ["okay","strict", "neglectful", "okay"]
    elif runs1 == 3:
        scenario = "Pen thief alert! Mark has been caught with two of his classmates' favorite pens. He claims he was just holding them for safekeeping."
        options = [
            "A. Make Mark return the pens and apologize.",
            "B. Ignore it, maybe the pens needed a new home.",
            "C. Hold a class meeting on the importance of sharing.",
            "D. Let Mark safekeep them."
        ]
        scores= ["okay","neglectful", "strict", "childish"]
    elif runs1 == 4:
        scenario = "Alex and Mia are playing doctor during recess. Mia is now diagnosing kids with homework flu and prescribing no homework for a week."
        options = [
            "A. Encourage their creativity and hand them a toy stethoscope.",
            "B. Call the school nurse to take over.",
            "C. Explain that doctors need to finish their work first.",
            "D. Laugh and tell them they should open a clinic."
        ]
        scores= ["motivational","neglectful", "okay", "childish"]
    elif runs1 == 5:
        scenario = "Leo thought it was a good idea to test if the toy car fits in his ear. Spoiler: It doesn't."
        options = [
            "A. Ask him if he wants to try the other ear.",
            "B. Give him a lecture on what ears are for.",
            "C. Call another teacher, this is above your pay grade.",
            "D. Send Leo to the nurse immediately."
        ]
        scores= ["childish","okay", "neglectful", "okay"]
    elif runs1 == 6:
        scenario = "Emily refuses to share her crayons with anyone, claiming she is building her own art empire."
        options = [
            "A. Ask Emily to politely share.",
            "B. Explain the magic of sharing.",
            "C. Trade a sticker for crayons.",
            "D. Help her build her empire."
        ]
        scores= ["okay","magical", "childish", "motivational"]
    elif runs1 == 7:
        scenario = "Ben has discovered the joy of scented markers and is now holding a sniffing contest during art class."
        options = [
            "A. Join the contest and declare a winner.",
            "B. Confiscate the markers and explain the dangers.",
            "C. Ignore it and let them have fun.",
            "D. Call the principal to handle it."
        ]
        scores= ["childish","strict", "neglectful", "strict"]
    elif runs1 == 8:
        scenario = "Sophia has decided to redecorate the classroom walls with her crayons."
        options = [
            "A. Praise her creativity and add your own drawing.",
            "B. Ask her to clean it up immediately.",
            "C. Call her parents to discuss her artistic tendencies.",
            "D. Ignore it and hope no one notices."
        ]
        scores= ["childish","strict", "motivational", "neglectful"]
    else:
        scenario = "No scenario available."
        options = []

    return scenario, options
    # "Jess claims Beatrice ate her homework"

def class_event():
    pass
