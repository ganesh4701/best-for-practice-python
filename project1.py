# Quiz on python questions
# using random module
# using input function to get user input
# ask the questions
# see if they are correct
# keep track of the score
# tell the user their score

import random


questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}

def ask_questions():
    questions_list = list(questions.keys())
    total_questions = len(questions_list)
    score = 0

    random_questions = random.sample(questions_list, total_questions)

    for idq, question in enumerate(random_questions,start=1):
        print(f'{idq}. {question}')
        user_answer = input('Your answer:').strip().lower()
        correct_answer = questions[question].strip().lower()
        if user_answer == 'exit':
            print('Exiting the game.')
            return
        elif user_answer == 'skip':
            print('Skipping question.')
            continue
        elif user_answer == 'hint':
            print(f'Hint: The answer starts with "{correct_answer[0]}"')
            user_answer = input('Your answer:').strip().lower()
        elif user_answer == correct_answer:
            print('correct answer')
            score += 1
        else:
            print(f'Wrong answer. The correct answer is: {correct_answer}')
    print("Game over! your score is: {}/{}".format(score,total_questions))

ask_questions()