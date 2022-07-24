from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
PURPLE = '#531A50'
AMETYST = '#9966CC'

class QuizInterface:
    # quiz_brain: QuizBrain - данная конструкция позволяет проверять тип переменной
    # в нашем случае это наш собственный класс, который мы любезно импортировали вверху
    # Пригодится это нам внизу, где мы вызываем метод quizbrainа

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window config
        self.window = Tk()
        self.window.title('VaporKiller Quiz')
        self.window.config(padx=20, pady=20, bg=PURPLE)

        # Label
        self.score = Label(text='PLACEHOLDER', fg='white', bg=PURPLE)
        self.score.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg=PURPLE, highlightthickness=0)
        image = PhotoImage(file='images/vaporwave.png')
        self.canvas.create_image(150, 125, image=image)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Some question',
            fill='white',
            font=('Courier', 20, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=50, pady=50)

        # Buttons and images
        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_butt)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_butt)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You reached the end of the quiz!')

    def true_butt(self):
        self.quiz.check_answer('True')
        self.get_next_question()

    def false_butt(self):
        self.quiz.check_answer('False')
        self.get_next_question()