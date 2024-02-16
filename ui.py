from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizGUI:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler!")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(width=350, height=320, background="white")
        self.canvas_text = self.canvas.create_text(175, 160, font=('Ariel 20 italic'), justify="center", width=300)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.score_label = Label(text=f"Score: {self.quiz.score}", background=THEME_COLOR, fg="white")
        self.right_button = Button(image=true_image, command=lambda: self.check_answer("true"),
                                   highlightbackground=THEME_COLOR)
        self.wrong_button = Button(image=false_image, command=lambda: self.check_answer("false"),
                                   highlightbackground=THEME_COLOR)

        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=50, pady=50)
        self.right_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def check_answer(self, answer: str):
        if self.quiz.check_answer(answer):
            self.canvas.config(bg="green", highlightcolor="green")
        else:
            self.canvas.config(bg="red", highlightcolor="red")
        self.window.after(2000, self.get_next_question)
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

    def get_next_question(self):
        try:
            self.canvas.config(background="white")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=question_text)
        except IndexError:
            self.canvas.itemconfig(self.canvas_text, text="You have reached the end of the quiz")
            self.wrong_button.config(state=DISABLED)
            self.right_button.config(state=DISABLED)
