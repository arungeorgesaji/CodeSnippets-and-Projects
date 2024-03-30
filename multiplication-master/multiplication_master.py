import customtkinter as ctk  
import random

score_counter = 0 

def problem():
    global ans
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    ans = x * y
    question = f"What is {x} * {y}?"
    return question

def check_answer():
    global score_counter
    user_answer = entry.get()
    try:
        user_answer = int(user_answer)
        if user_answer == ans:
            result_label.configure(text="Correct!", text_color="green")
            score_counter += 1
            score.configure(text="Score:" + str(score_counter))
        else:
            result_label.configure(text=f"Incorrect, the correct answer was {ans}", text_color="red")
            score.configure(text="Score:0")

        label.configure(text=problem()) 

    except ValueError:
        result_label.configure(text="Please enter a valid number", text_color="red")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()  
root.title("Multiplication Master")
root.geometry("620x340")
root.after(201, lambda: root.iconbitmap("mm_logo.ico"))

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text=problem())
label.pack(pady=10, padx=10)
label.configure(font=("Roberta", 50))

entry = ctk.CTkEntry(master=frame, placeholder_text="Type the answer")
entry.pack(pady=12, padx=10)

check_button = ctk.CTkButton(master=frame, text="Check Answer", command=check_answer)
check_button.pack(pady=10, padx=10)

result_label = ctk.CTkLabel(master=frame, text="")
result_label.pack(pady=30, padx=10)
result_label.configure(font=("Roberta", 20))

score = ctk.CTkLabel(master=frame, text="Score:0")
score.pack(pady=0, padx=10) 
score.configure(font=("Roberta", 20))

root.mainloop()
