from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # UI

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0, columnspan=2)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(150, 125, width=250, text="This is a Question", font=("Arial", 12, "italic"))

        img_yes = PhotoImage(file="./images/true.png")
        self.button_yes = Button(image=img_yes, highlightthickness=0, relief="flat", border=0)
        self.button_yes.grid(column=0, row=2)

        img_no = PhotoImage(file="./images/false.png")
        self.button_no = Button(image=img_no, highlightthickness=0, relief="flat", border=0)
        self.button_no.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
 