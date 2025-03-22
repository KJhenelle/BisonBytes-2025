import random
import tkinter as tk
from tkinter import messagebox


events = [
    {
        "question": "The principal walks in unexpectedly. What do you do?",
        "choices": [
            "A. Continue the lesson calmly as if nothing happened (correct)",
            "B. Panic and tell students to behave immediately",
            "C. Stop teaching and ask the principal what she needs",
            "D. Whisper to the class stating to be on their best behavior"
        ],
        "correct": "A"
    },
    {
        "question": "A new student joins your class. What’s the best approach?",
        "choices": [
            "A. Let student quietly observe and settle in.",
            "B. Ask them to introduce themselves immediately",
            "C. Give them a tour of the classroom",
            "D. Introduce them yourself and assign a buddy to help (correct)"
        ],
        "correct": "D"
    },
    {
        "question": "Two students start fighting during class. What’s your move?",
        "choices": [
            "A. Yell at them to both stop immediately",
            "B. Separate them and address them calmly (correct)",
            "C. Send both to the principal's office",
            "D. Ignore it and hope they stop"
        ],
        "correct": "B"
    },
    {
        "question": "A student shows signs of chickenpox. What’s your immediate action?",
        "choices": [
            "A. Send student to the nurse immediately (correct)",
            "B. Tell student to wait till lunch",
            "C. Announce to class that there is an outbreak",
            "D. Give them a tissue and tell them to wait patiently"
        ],
        "correct": "A"
    },
    {
        "question": "You get a reminder about a parent-teacher conference. What do you do?",
        "choices": [
            "A. Reschedule and send a polite apology (correct)",
            "B. Wing it and hope for the best",
            "C. Ask another teacher to cover it",
            "D. Gaslight them and pretend it wasn’t scheduled"
        ],
        "correct": "A"
    },
    {
        "question": "Tech failure during a lesson. What’s your next step?",
        "choices": [
            "A. Continue the lesson without the tech (correct)",
            "B. Spend 10 minutes trying to fix it",
            "C. Let the class take a break while you find a solution",
            "D. Call it and cancel the lesson"
        ],
        "correct": "A"
    }
]


# function to randomly trigger events

def trigger_event():
    event = random.choice(events)
    ask_question(event)


# function to display a random pop-up question
def ask_question(event):
    def check_answer(selected_choice):
        if selected_choice == event["correct"]:
            messagebox.showinfo("Result", "Correct Answer!")
        else:
            messagebox.showinfo("Result", "Wrong Answer! Try Again.")
    
    question_window = tk.Toplevel(root)
    question_window.title("Unexpected!")
    question_label = tk.Label(question_window, text=event["question"], font=("Arial", 14), wraplength=500)
    question_label.pack(pady=10)

    # Create buttons for choices
    for index, choice in enumerate(event["choices"]):
        button = tk.Button(question_window, text=choice, font=("Arial", 12), 
                           command=lambda choice=choice[0]: check_answer(choice))
        button.pack(pady=5)
