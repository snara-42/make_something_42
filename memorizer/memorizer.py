import argparse
import random
from quizdata import projects, writing_systems


# does not save
# def add_function(function, header, subject):
#     if subject in projects:
#         projects[subject][function] = header
#         print(f"Added: {function} -> {header} to subject {subject}")
#     else:
#         projects[subject] = {function: header}
#         print(f"Added new subject {subject} with: {function} -> {header}")


def view_functions(subject=None):
    if subject:
        if subject in projects:
            for function, header in projects[subject].items():
                print(f"{function} -> {header}")
        else:
            print(f"Subject {subject} not found.")
    else:
        for subject, funcs in projects.items():
            print(f"\nSubject: {subject}")
            for function, header in funcs.items():
                print(f"{function} -> {header}")


def list_subjects():
    subjects = list(projects.keys()) + list(writing_systems.keys())
    for i, subject in enumerate(subjects):
        print(f"{i+1}. {subject}")
    return subjects


def quiz(subject: str):
    if subject in projects:
        quiz_headerfile(subject)
    elif subject in writing_systems:
        quiz_characters(writing_systems[subject])
    else:
        print(f"Subject {subject} not found.")
        return


def quiz_headerfile(subject: str):
    # Track functions that were answered incorrectly or not answered yet
    functions = list(projects[subject].keys())
    incorrect_answers = set(functions)

    print("(enter 'quit' to stop)")
    while incorrect_answers:
        random_function = random.choice(list(incorrect_answers))
        print(f"Which header does '{random_function}' belong to? ", end="")
        user_input = input().strip()
        if user_input.lower() == 'quit':
            print("Quiz ended.")
            break
        elif projects[subject][random_function] in [user_input, user_input+".h"]:
            print("Correct!")
            incorrect_answers.remove(random_function)  # Remove correct answer from the set
        else:
            print(f"Incorrect. The correct answer is '{projects[subject][random_function]}'.")

    if not incorrect_answers:
        print("You have answered all questions correctly for this subject!")


def quiz_characters(characters: dict):
    incorrect_answers = set(characters.keys())

    print("(enter 'quit' to stop)")
    while incorrect_answers:
        random_char = random.choice(list(incorrect_answers))
        print(f"How do you pronounce [{random_char}] ? ", end="")
        user_input = input().strip()
        if user_input.lower() == 'quit':
            print("Quiz ended.")
            break
        elif user_input in characters[random_char]:
            print("Correct!")
            incorrect_answers.remove(random_char)
        else:
            print(f"Close! The correct answer is {characters[random_char]}.")

    if not incorrect_answers:
        print("You have answered all questions correctly for this writing system!")


def main():
    parser = argparse.ArgumentParser(description='CLI for memorizing library functions and headers.')
    parser.add_argument('--view', nargs='?', const=True, metavar='SUBJECT',
                        help='View all functions and headers, optionally for a specific subject')
    parser.add_argument('--quiz', nargs='?', const=True, metavar='SUBJECT',
                        help='Quiz yourself on functions and headers for a specific subject')

    args = parser.parse_args()

    if args.view:
        if args.view is True:
            view_functions()
        else:
            view_functions(args.view)
    elif args.quiz:
        if args.quiz is True:
            print("Please choose a subject from the list below by number:")
            subjects = list_subjects()
            try:
                choice = int(input("Enter the number of the subject: ")) - 1
                if not 0 <= choice < len(subjects):
                    raise ValueError
                args.quiz = subjects[choice]
            except ValueError and IndexError:
                print("Invalid input. Please enter a valid number.")
                return
        quiz(args.quiz)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
