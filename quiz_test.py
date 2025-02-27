import random
#import matplotlib.pyplot as plt

import matplotlib
#matplotlib.use('Agg')  # Use 'Agg' backend to avoid Tkinter issues
import matplotlib.pyplot as plt


# Function to load questions from a file
def load_questions(filename):
    questions = {}
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(" - ")  # Use ' - ' as separator
                if len(parts) == 2:
                    question, answer = parts
                    questions[question] = answer
    except FileNotFoundError:
        print("Error: Questions file not found!")
    return questions

# Function to conduct the quiz
def Quiz_test(subject, filename):
    questions_and_answers = load_questions(filename)

    if not questions_and_answers:
        print("No questions found! Please check the file.")
        return 0

    question_list = list(questions_and_answers.keys())
    total_question = min(10, len(question_list))  # Ensure we don't ask more than available questions
    score = 0

    # Select random questions
    selected_question = random.sample(question_list, total_question)

    # Ask the questions
    for ques_number, question in enumerate(selected_question):
        print(f"{ques_number+1}. {question}")
        user_answer = input("Your answer: ").lower().strip()

        correct_answer = questions_and_answers[question]

        if user_answer == correct_answer.lower():
            print("Correct Answer!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.\n")

    print(f"Final score in {subject} : {score}/10")
    return score

# List of subjects and their corresponding file names
quiz_topics = [
    ("GK", "questions_gk.txt"),
    ("C++", "questions_cpp.txt"),
    ("Python", "questions_python.txt"),
    ("Math", "questions_math.txt"),
    ("Java", "questions_java.txt")
]

quiz_result = {}

for subject, question_bank in quiz_topics :
    quiz_result[subject] = Quiz_test(subject, question_bank)


def plot_combined_results(result):
    subjects = list(result.keys())
    scores = list(result.values())

    total_marks = sum(scores)
    remaining_marks = len(subjects) * 10 - total_marks  # Total possible marks - achieved marks
    labels = ["Achieved", "Remaining"]
    sizes = [total_marks, remaining_marks]
    colors = ["green", "lightgray"]

    # Create a figure with 2 subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    # Bar Chart (Left Side)
    axs[0].bar(subjects, scores, color=['green', 'red', 'blue', 'purple', 'yellow'])
    axs[0].set_xlabel("Subjects")
    axs[0].set_ylabel("Score (Out of 10)")
    axs[0].set_title("Quiz Scores by Subject")
    axs[0].set_ylim(0, 10)

    # Pie Chart (Right Side)
    axs[1].pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    axs[1].set_title("Total Score Distribution")

    plt.tight_layout()
    plt.show()

# Call the new function
plot_combined_results(quiz_result)


# Run the quiz




