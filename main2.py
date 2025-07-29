from src.QA import Quiz, QA
import argparse

quiz = Quiz(
        [
            QA(
                question="What is the capital of France?",
                answers={"a": "Paris", "b": "London", "c": "Berlin", "d": "Madrid"},
                right_answer="a"
            ),
            QA(
                question="What is the capital of Germany?",
                answers={"a": "London", "b": "Paris", "c": "Berlin", "d": "Rome"},
                right_answer="c"
            ),
            QA(
                question="What is the capital of Italy?",
                answers={"a": "Paris", "b": "Rome", "c": "London", "d": "Berlin"},
                right_answer="b"
            ),
            QA(
                question="What is the capital of Spain?",
                answers={"a": "Rome", "b": "Paris", "c": "London", "d": "Madrid"},
                right_answer="d"
            ),
            QA(
                question="What is the capital of Portugal?",
                answers={"a": "Lisbon", "b": "Paris", "c": "London", "d": "Madrid"},
                right_answer="a"
            ),
            QA(
                question="What is the capital of Poland?",
                answers={"a": "Warsaw", "b": "Paris", "c": "London", "d": "Madrid"},
                right_answer="a"
            ),
            QA(
                question="What is the capital of Romania?",
                answers={"a": "Bucharest", "b": "Paris", "c": "London", "d": "Madrid"},
                right_answer="a"
            ),
            QA(
                question="What is the capital of Greece?",
                answers={"a": "Athens", "b": "Paris", "c": "London", "d": "Madrid"},
                right_answer="a"
            )
        ]
    )

def main():
    parser = argparse.ArgumentParser(
        description="Generate a quiz from a user query."
    )

    parser.add_argument(
        "--num_questions", "-n",
        type=int,
        default=5,
        help="Number of questions to generate."
    )

    args = parser.parse_args()

    score = 0
    for qa in quiz.qa_list[:args.num_questions]:
        print(qa)
        answer = input("Enter your answer: ")
        if qa.check_answer(answer):
            score += 1
    print(f"You got {score} out of {args.num_questions} questions correct")

if __name__ == "__main__":
    main()
    