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
q3: Question = Question("", "", ("", "", ""))
q4: Question = Question("", "", ("", "", ""))
q5: Question = Question("", "", ("", "", ""))
q6: Question = Question("", "", ("", "", ""))
q7: Question = Question("", "", ("", "", ""))
q8: Question = Question("", "", ("", "", ""))
q9: Question = Question("", "", ("", "", ""))
q10: Question = Question("", "", ("", "", ""))

q11: Question = Question("", "", ("", "", ""))
q12: Question = Question("", "", ("", "", ""))
q13: Question = Question("", "", ("", "", ""))
q14: Question = Question("", "", ("", "", ""))
q15: Question = Question("", "", ("", "", ""))
q16: Question = Question("", "", ("", "", ""))
q17: Question = Question("", "", ("", "", ""))
q18: Question = Question("", "", ("", "", ""))
q19: Question = Question("", "", ("", "", ""))
q20: Question = Question("", "", ("", "", ""))

q21: Question = Question("", "", ("", "", ""))
q22: Question = Question("", "", ("", "", ""))
q23: Question = Question("", "", ("", "", ""))
q24: Question = Question("", "", ("", "", ""))
q25: Question = Question("", "", ("", "", ""))
q26: Question = Question("", "", ("", "", ""))
q27: Question = Question("", "", ("", "", ""))
q28: Question = Question("", "", ("", "", ""))
q29: Question = Question("", "", ("", "", ""))
q30: Question = Question("", "", ("", "", ""))

question_list: List[Question] = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19,
                                 q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30]
