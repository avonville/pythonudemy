from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.theme_color = "#375362"
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=self.theme_color)
        self.score_labal = Label(text=f"Score: {self.quiz.score}", bg=self.theme_color, fg="white" )
        self.score_labal.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text( 
            150,
            125,
            width=280,
            text="Question Text", 
            font=("Arial",20,"italic"), 
            fill=self.theme_color
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        button_wrong_img = PhotoImage(file=r"images\false.png")
        self.button_wrong = Button(image=button_wrong_img, highlightthickness=0, command=self.press_false)
        self.button_wrong.grid(column=0, row=2)
        button_right_img = PhotoImage(file=r"images\true.png")
        self.button_right = Button(image=button_right_img, highlightthickness=0, command=self.press_true)
        self.button_right.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score_labal.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Final Score: {self.quiz.score} / 10")
            self.button_wrong.config(state="disabled")
            self.button_right.config(state="disabled")
        
    def press_false(self):
        self.give_feedback(self.quiz.check_answer("false"))
   
    def press_true(self):
        self.give_feedback(self.quiz.check_answer("true"))        
    
    def give_feedback(self, answer):
        if answer:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
