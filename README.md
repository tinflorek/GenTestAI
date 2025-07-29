# GenTestAI

GenTestAI is a command-line tool that generates multiple-choice quizzes from the content of a text file using AI. It leverages OpenAI's GPT models to create questions and answers, making it useful for educators, students, and anyone looking to test their knowledge on a given topic.

## Features
- Automatically generates multiple-choice questions from any text file
- Customizable number of questions
- Interactive quiz mode with answer checking

## Prerequisites
- Python 3.8+
- An OpenAI API key (for GPT-3.5/4 access)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/GenTestAI.git
   cd GenTestAI
   ```
2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set your OpenAI API key as an environment variable. You can do this by creating a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage
1. Prepare a text file containing the content you want to generate a quiz from (e.g., `sample.txt`).
2. Run the program from the command line:
   ```bash
   python main.py --file sample.txt --num_questions 5
   ```
   - `--file` or `-f`: Path to the text file to base the quiz on (required)
   - `--num_questions` or `-n`: Number of questions to generate (default: 5)
3. The program will display each question and prompt you to enter your answer. At the end, your score will be shown.

## Example
```bash
python main.py --file my_notes.txt --num_questions 3
```

## License
This project is licensed under the MIT License. 