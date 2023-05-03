from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from quiz_brain import QuizBrain
# import datetime

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("TYT Bio Evren Quiz")
        self.window.geometry("850x530")

        self.display_title()

        self.canvas = Canvas(width=800, height=250)
        self.question_text = self.canvas.create_text(400, 125,
                                                     text="Question here",
                                                     width=680,
                                                     fill=THEME_COLOR,
                                                     font=(
                                                         'Ariel', 14, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        self.user_answer = StringVar()

        self.opts = self.radio_buttons()
        self.display_options()

        self.feedback = Label(self.window, pady=20, font=("ariel", 12, "bold"))
        self.feedback.place(x=300, y=380)

        self.buttons()

        self.window.mainloop()

    def display_title(self):

        title = Label(self.window, text="TYT Bio Evren Quiz",
                      width=50, bg="#816BF4", fg="white", font=("ariel", 20, "bold"))

        title.place(x=-50, y=2)

    def display_question(self):

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def radio_buttons(self):
        choice_list = []

        y_pos = 220

        while len(choice_list) < 4:

            radio_btn = Radiobutton(self.window, text="", variable=self.user_answer,
                                    value='', font=("ariel", 14))

            choice_list.append(radio_btn)

            radio_btn.place(x=200, y=y_pos)

            y_pos += 40

        return choice_list

    def display_options(self):

        val = 0

        self.user_answer.set(None)

        for option in self.quiz.current_question.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    def next_btn(self):
        """To show feedback for each answer and keep checking for more questions"""

        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Doğru Cevap!'
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = ('Yanlış Cevap! \n'
                                     f'Doğru Seçenek: {self.quiz.current_question.correct_answer}')

        if self.quiz.has_more_questions():
            self.display_question()
            self.display_options()
        else:
            self.display_result()

            self.window.destroy()

    def buttons(self):
        next_button = Button(self.window, text="Sıradaki Soru", command=self.next_btn,
                             width=13, bg="#998BE4", fg="white", font=("ariel", 14, "bold"), border=.5)

        next_button.place(x=350, y=470)

        quit_button = Button(self.window, text="Çıkış Yap", command=self.window.destroy,
                             width=9, bg="red", fg="white", font=("ariel", 11, " bold"))

        quit_button.place(x=710, y=65)

    def display_result(self):
        correct, wrong, score_percent = self.quiz.get_score()

        correct = f"Doğru Sayısı: {correct}"
        wrong = f"Yanlış Sayısı: {wrong}\n"

        result = f"Skorunuz: {score_percent}%"

        messagebox.showinfo("Sonuç", f"{result}\n{correct}\n{wrong}")
