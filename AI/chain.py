import os
from typing import List, Dict, Any
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from src.QA import QA, Quiz
import dotenv

dotenv.load_dotenv()

class QAModel(BaseModel):
    question: str = Field(description="The question for the quiz.")
    answers: Dict[str, str] = Field(description="A dictionary of possible answers, where keys are labels (e.g., 'A', 'B', 'C') and values are the answer texts.")
    right_answer: str = Field(description="The label (e.g., 'A') corresponding to the correct answer.")

class QuizModel(BaseModel):
    questions: List[QAModel] = Field(description="A list of multiple-choice questions.")

parser = JsonOutputParser(pydantic_object=QuizModel)

prompt = PromptTemplate(
    template="Generate {num_questions} multiple-choice questions based on the following text content.\n{format_instructions}\nText Content: {text_content}\n",
    input_variables=["num_questions", "text_content"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))

chain = prompt | llm | parser

def generate_quiz(num_questions: int, text_content: str) -> Quiz:
    llm_output_dict = chain.invoke({"num_questions": num_questions, "text_content": text_content})
    qa_instances = []
    for q_data in llm_output_dict['questions']:
        qa_instances.append(
            QA(
                question=q_data['question'],
                answers=q_data['answers'],
                right_answer=q_data['right_answer']
            )
        )
    return Quiz(qa_instances)