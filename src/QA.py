from typing import Dict, List

class QA:
    def __init__(self, question: str, answers: Dict[str, str], right_answer: str) -> None:
        self.question = question
        self.answers = answers
        self.right_answer = right_answer

    def __str__(self) -> str:
        answers_str = ", ".join([f"{k}: {v}" for k, v in self.answers.items()])
        return f"Question: {self.question}\nAnswers: {{{answers_str}}}"

    def check_answer(self, answer: str) -> bool:
        return answer.lower() == self.right_answer.lower()

class Quiz:
    def __init__(self, qa_list: List[QA]) -> None:
        self.qa_list = qa_list

    def __str__(self) -> str:
        quiz_str = "--- Quiz ---\n"
        for i, qa in enumerate(self.qa_list):
            quiz_str += f"\nQuestion {i+1}:\n{qa}\n"
        quiz_str += "------------"
        return quiz_str