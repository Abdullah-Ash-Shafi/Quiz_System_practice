# Quiz System with Results Visualization

This project is a quiz system that allows users to take quizzes on various subjects, track their scores, and visualize the results using both bar charts and pie charts. The quiz data is read from external text files, and random questions are selected for the quiz. After the quiz, a visualization is generated to display the results.

## Features

- Randomly selects questions from a predefined set of questions stored in text files.
- Conducts quizzes on multiple subjects (e.g., General Knowledge, C++, Python, Math, Java).
- Tracks the user's score for each subject.
- Generates a bar chart displaying the scores for each subject.
- Generates a pie chart to visualize the total score distribution.
- Provides feedback after each answer (correct or incorrect).
- Outputs the final score at the end of the quiz.

## Project Structure

- `quiz_system.py`: The main script that handles quiz execution, user input, and score tracking.
- `questions_gk.txt`: A file containing General Knowledge questions and answers (format: `Question - Answer`).
- `questions_cpp.txt`: A file containing C++ programming questions and answers.
- `questions_python.txt`: A file containing Python programming questions and answers.
- `questions_math.txt`: A file containing Math-related questions and answers.
- `questions_java.txt`: A file containing Java programming questions and answers.
- `README.md`: This file.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/quiz-system.git
   ```

2. Install the required Python libraries:
   ```bash
   pip install matplotlib
   ```

3. Make sure you have the question files (`questions_gk.txt`, `questions_cpp.txt`, `questions_python.txt`, `questions_math.txt`, `questions_java.txt`) in the same directory as the script or adjust the file paths accordingly.

## Usage

1. Open the `quiz_system.py` script in a Python environment.
2. The quiz will automatically start and ask you to answer 10 random questions for each subject.
3. Answer each question by typing your response and hitting Enter.
4. After completing the quiz, your score will be displayed for each subject.
5. A bar chart and pie chart will be generated showing your performance.

### Example Output:

- **Quiz Score Feedback:**
  ```
  1. What is the capital of France?
  Your answer: Paris
  Correct Answer!

  Final score in General Knowledge : 8/10
  ```

- **Result Visualization:**
  - **Bar Chart**: Displays your score in each subject.
  - **Pie Chart**: Shows the percentage of total marks achieved versus the remaining marks.

