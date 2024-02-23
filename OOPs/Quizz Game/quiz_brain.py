class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.false_answer = []

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f'Q{self.question_number + 1}. {current_question.text} (True/False):\n').title()
        while answer not in ['True', 'False']:
            answer = input(
                f'Please enter True or False only!\nQ{self.question_number + 1}. {current_question.text}'
                f' (True/False):\n').title()
        self.check_answer(answer, current_question)

    def check_answer(self, user_answer, current_question):
        if user_answer == current_question.answer:
            self.score += 1
        else:
            self.false_answer.append({'question': current_question.text, 'correct_answer': current_question.answer,
                                      'user_answer': user_answer})

    def print_result(self):
        print(f"Your score is {self.score}\n")
        if self.false_answer is not None:
            print("Let's review the questions you got wrong:")
            for i in range(len(self.false_answer)):
                print(
                    f"Q. {self.false_answer[i]['question']} \nCorrect answer: {self.false_answer[i]['correct_answer']}"
                    f"\nYour answer is: {self.false_answer[i]['user_answer']}")
