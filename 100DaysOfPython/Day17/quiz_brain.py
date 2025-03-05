class QuizBrain:
    def __init__(self, list) -> None:
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def still_has_questions(self):
        """This function checks to see that there are still questions in the the question bank"""
        return self.question_number < len(self.question_list)

    def next_question(self):
       """This function goes to the next question in the list"""
       current_question = self.question_list[self.question_number]
       self.question_number += 1
       user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")
       self.check_answer(user_answer, current_question.answer)
       
    

    def check_answer(self, user_answer, correct_answer):
        """This function caompares the user provided answer to the correct answer"""
        if user_answer.lower() == correct_answer.lower():
            print("You are right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current {self.score}/{self.question_number} \n")