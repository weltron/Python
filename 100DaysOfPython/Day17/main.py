from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    quiz = Question(question['question'], question['correct_answer'])
    question_bank.append(quiz)
    

new = QuizBrain(question_bank)

while new.still_has_questions():
    new.next_question()

print("You've completed the quiz")
print(f"Your final score is {new.score}/{new.question_number}")