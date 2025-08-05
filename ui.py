from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.timer = None

        # UI

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0, columnspan=2)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(150, 125, width=250, text="This is a Question", font=("Arial", 15, "bold italic"), fill=THEME_COLOR)

        img_yes = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=img_yes, highlightthickness=0, relief="flat", border=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        img_no = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=img_no, highlightthickness=0, relief="flat", border=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.reset_canvas()
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)            
            self.update_score()
        else:
            self.canvas.itemconfig(self.question_text, text="You've reach the end of the Quiz.", font=("Arial", 24, "bold italic"))
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer(str(True))
        self.give_feedback(is_right)        

    def false_pressed(self):
        is_right = self.quiz.check_answer(str(False))
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#75880e")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="#ce1800")
            self.canvas.itemconfig(self.question_text, fill="white")

        if self.timer:
            self.window.after_cancel(self.timer)
        self.timer = self.window.after(1000, func=self.get_next_question)

    def reset_canvas(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
