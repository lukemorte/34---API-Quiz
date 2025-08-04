from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20)

        # UI

        score = Label(text="Score: 0")
        score.grid(column=1, row=0, columnspan=2)

        canvas = Canvas(width=300, height=250, bg="white")
        canvas.grid(column=1, row=1)

        question_text = canvas.create_text(150, 125, width=100, text="This is a Question", font=("Arial", 20, "italic"))


        self.window.mainloop()
