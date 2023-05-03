from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from random import shuffle

question_bank = []
for question in question_data:
    choices = []
    question_text = question["question"]
    correct_answer = question["correct_answer"]
    incorrect_answers = question["incorrect_answers"]

    question_text = question_text.replace("Ä°","İ")
    question_text = question_text.replace("Ä±","ı")
    question_text = question_text.replace("Ã§","ç")
    question_text = question_text.replace("ÅŸ","ş")
    question_text = question_text.replace("ÄŸ","ğ")
    question_text = question_text.replace("Åž","Ş")
    question_text = question_text.replace("Äž","Ğ")
    question_text = question_text.replace("Ã¶","ö")
    question_text = question_text.replace("Ã¼","ü")
    question_text = question_text.replace("Ã‡","Ç")
    question_text = question_text.replace("Ã¼","ü")
    question_text = question_text.replace("â€¢","•")
    question_text = question_text.replace("Ã–","Ö")
    

    correct_answer = correct_answer.replace("Ä°","İ")
    correct_answer = correct_answer.replace("Ä±","ı")
    correct_answer = correct_answer.replace("Ã§","ç")
    correct_answer = correct_answer.replace("ÅŸ","ş")
    correct_answer = correct_answer.replace("ÄŸ","ğ")
    correct_answer = correct_answer.replace("Åž","Ş")
    correct_answer = correct_answer.replace("Äž","Ğ")
    correct_answer = correct_answer.replace("Ã¶","ö")
    correct_answer = correct_answer.replace("Ã¼","ü")
    correct_answer = correct_answer.replace("Ã‡","Ç")
    correct_answer = correct_answer.replace("Ã¼","ü")
    correct_answer = correct_answer.replace("Ã–","Ö")
    



    # print(question_text)
    for ans in incorrect_answers:
        ans = ans.replace("Ä°","İ")
        ans = ans.replace("Ä±","ı")
        ans = ans.replace("Ã§","ç")
        ans = ans.replace("ÅŸ","ş")
        ans = ans.replace("ÄŸ","ğ")
        ans = ans.replace("Åž","Ş")
        ans = ans.replace("Äž","Ğ")
        ans = ans.replace("Ã¶","ö")
        ans = ans.replace("Ã¼","ü")
        ans = ans.replace("Ã‡","Ç")
        ans = ans.replace("Ã¼","ü")
        ans = ans.replace("Ã–","Ö")

        choices.append(ans)

    choices.append(correct_answer)
    shuffle(choices)
    new_question = Question(question_text, correct_answer, choices)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

print("Quiz Sona Erdi!")
print(f"Sonucunuz: {quiz.score}/{quiz.question_no}")