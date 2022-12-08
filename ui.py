from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    """a class that sets the GUI for the main file of the project"""
    def __init__(self, quiz_brain: QuizBrain):
        """Initialize the attributes for QuizInterface"""
        self.question = quiz_brain

        self.window = Tk()
        self.window.title("Reed's Trivia Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # create a label
        self.score_label = Label(text=f"Score: {self.question.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # create a canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text=f"Reed is so handsome",
            fill=THEME_COLOR,
            width=260,
            font=FONT,
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        # import image
        false_image = PhotoImage(file="./images/false.png")
        true_image = PhotoImage(file="./images/true.png")
        # create buttons
        self.true_button = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR, command=self.press_true)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_image, highlightthickness=0, bg=THEME_COLOR, command=self.press_false)
        self.false_button.grid(row=2, column=1)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        """displays the current question on the screen"""
        self.canvas.config(bg="white")
        if self.question.still_has_questions():
            self.score_label.config(text=f"Score: {self.question.score}")
            question_text = self.question.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.score_label.config(text=f"Score: {self.question.score}")
            self.canvas.itemconfig(self.question_text, text=f"You've finished the quiz. "
                                                            f"Final score: {self.question.score}/"
                                                            f" {self.question.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def press_true(self):
        """sets the user answer to true and compares to the correct answer"""
        answer = "true"
        self.give_feedback(self.question.check_answer(answer))

    def press_false(self):
        """sets the user answer to false and compares to the correct answer"""
        self.give_feedback(self.question.check_answer("false"))

    def give_feedback(self, is_right: bool):
        """gives a feedback to the user whether the answer is right or wrong"""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.next_question)
