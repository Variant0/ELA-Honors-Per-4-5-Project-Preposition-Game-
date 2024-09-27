from typing import Tuple, List


class Question:
    def __init__(self, question: str, ans: str, wr_ans: Tuple[str, str, str]):
        self.question = question
        self.ans = ans
        self.wr_ans = wr_ans

    def get_arg_question(self) -> str:
        return self.question

    def get_arg_ans(self) -> str:
        return self.ans

    def get_arg_wr_ans(self) -> Tuple[str, str, str]:
        return self.wr_ans

    def copy(self):
        return Question(self.question, self.ans, self.wr_ans)


# Question Pool
q1: Question = Question("Which of the following is a preposition?", "to", ("and", "desk", "run"))
q2: Question = Question("Which is a compound preposition?", "next to", ("near me", "then", "here"))
q3: Question = Question("I was born ____ May.", "in", ("on", "at", "previously"))
q4: Question = Question("They climbed ____ the highest hill.", "up", ("under", "above", "for"))
q5: Question = Question("We got married ___ our son was born.", "before", ("within", "up", "during"))
q6: Question = Question("The farmer wakes up ____ sunrise.", "at", ("on", "of", "for"))
q7: Question = Question("The river Thames flows ____ London.", "through", ("on", "over", "of"))
q8: Question = Question("Which of the following is a preposition?", "between", ("very", "soon", "fast"))
q9: Question = Question("Which of the following is a preposition?", "across", ("be", "say", "bald"))
q10: Question = Question("Which of the following is a preposition?", "often", ("calm", "fierce", "make"))

q11: Question = Question("Which of the following is a preposition?", "against", ("seriously", "take", "big"))
q12: Question = Question("Which is a compound preposition?", "in spite of", ("often", "daily", "on the way to"))
q13: Question = Question("Which is a compound preposition?", "aside from", ("around", "across", "hard battle"))
q14: Question = Question("Which is a compound preposition?", "as of", ("beside", "daily task", "angry"))
q15: Question = Question("Which is a compound preposition?", "because of", ("run", "twenty lamps", "defeated"))
q16: Question = Question("A prepositional phrase begins with a preposition.", "True", ("False", "", ""))
q17: Question = Question("A prepositional phrase can have modifiers.", "True", ("False", "", ""))
q18: Question = Question("A prepositional phrase can have an action word.", "False", ("True", "", ""))
q19: Question = Question("A compound prepositon has 2 or more words in it.", "True", ("False", "", ""))
q20: Question = Question("A preposition connects two nouns or pronouns.", "True", ("False", "", ""))

q21: Question = Question("A prepositional phrase starts/ends with a preposition.", "True", ("False", "", ""))
q22: Question = Question("A prepositional phrase must have an object.", "True", ("False", "", ""))
q23: Question = Question("Which of the following is a preposition?", "beside", ("rarely", "kind", "lively"))
q24: Question = Question("Which is a compound preposition", "instead of", ("eventually", "sometimes go", "book cases"))
q25: Question = Question("A prepositional phrase has to be 3 words", "False", ("True", "", ""))
q26: Question = Question("The bird is ______ the cage.", "within", ("true", "real", "wide"))
q27: Question = Question("Which is a compound preposition?", "because of", ("around", "under the", "about ten"))
q28: Question = Question("Which is a preposition?", "beneath", ("the", "thoughtless", "tiny"))
q29: Question = Question("Which is a modifier?", "the", ("run", "walk", "talk"))
q30: Question = Question("Which is a modifier?", "a", ("sprint", "kick", "enjoy"))

question_list: List[Question] = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19,
                                 q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30]
