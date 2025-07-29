from src.QA import QA
from AI.chain import chain, generate_quiz
import argparse
import os

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

    parser.add_argument(
        "--file", "-f", 
        type=str,
        required=True,
        help="File on which the quiz will be based."
    )

    args = parser.parse_args()

    quiz = generate_quiz(args.num_questions, args.file)

    score = 0

    for qa in quiz.qa_list:
        print(qa)
        answer = input("Enter your answer: ")
        if qa.check_answer(answer):
            score += 1
    print(f"You got {score} out of {args.num_questions} questions correct")

if __name__ == "__main__":
    main()