import argparse
import random

# Dictionary to store functions and headers for quizzes
projects = {
    "libft": {
        "malloc": "stdlib.h",
        "free": "stdlib.h",
        "write": "unistd.h",
    },
    "get_next_line": {
        "malloc": "stdlib.h",
        "free": "stdlib.h",
        "read": "unistd.h",
    },
    "ft_printf": {
        "malloc": "stdlib.h",
        "free": "stdlib.h",
        "write": "unistd.h",
        "va_start": "stdarg.h",
        "va_arg": "stdarg.h",
        "va_copy": "stdarg.h",
        "va_end": "stdarg.h",
    },
    "minishell": {
        "readline": "readline.h",
        "rl_clear_history": "readline.h",
        "rl_on_new_line": "readline.h",
        "rl_replace_line": "readline.h",
        "rl_redisplay": "readline.h",
        "add_history": "readline.h",

        "printf": "stdio.h",
        "malloc": "stdlib.h",
        "free": "stdlib.h",

        "write": "unistd.h",
        "access": "unistd.h",
        "open": "fcntl.h",
        "read": "unistd.h",
        "close": "unistd.h",

        "fork": "unistd.h",
        "wait": "sys/wait.h",
        "waitpid": "sys/wait.h",
        "wait3": "sys/wait.h",
        "wait4": "sys/wait.h",

        "signal": "signal.h",
        "sigaction": "signal.h",
        "sigemptyset": "signal.h",
        "sigaddset": "signal.h",
        "kill": "signal.h",

        "exit": "stdlib.h",

        "getcwd": "unistd.h",
        "chdir": "unistd.h",

        "stat": "sys/stat.h",
        "lstat": "sys/stat.h",
        "fstat": "sys/stat.h",
        "unlink": "unistd.h",

        "execve": "unistd.h",
        "dup": "unistd.h",
        "dup2": "unistd.h",
        "pipe": "unistd.h",

        "opendir": "dirent.h",
        "readdir": "dirent.h",
        "closedir": "dirent.h",

        "strerror": "string.h",
        "perror": "stdio.h",

        "isatty": "unistd.h",
        "ttyname": "unistd.h",
        "ttyslot": "unistd.h",
        "ioctl": "sys/ioctl.h",

        "getenv": "stdlib.h",

        "tcsetattr": "termios.h",
        "tcgetattr": "termios.h",
        "tgetent": "curses.h term.h",
        "tgetflag": "curses.h term.h",
        "tgetnum": "curses.h term.h",
        "tgetstr": "curses.h term.h",
        "tgoto": "curses.h term.h",
        "tputs": "curses.h term.h",
    },
}

def add_function(function, header, subject):
    if subject in projects:
        projects[subject][function] = header
        print(f"Added: {function} -> {header} to subject {subject}")
    else:
        projects[subject] = {function: header}
        print(f"Added new subject {subject} with: {function} -> {header}")

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
    subjects = list(projects.keys())
    for i, subject in enumerate(subjects):
        print(f"{i+1}. {subject}")
    return subjects

def quiz(subject):
    if subject not in projects:
        print(f"Subject {subject} not found.")
        return

    functions = list(projects[subject].keys())
    incorrect_answers = set(functions)  # Track functions that were answered incorrectly or not answered yet

    while incorrect_answers:
        random_function = random.choice(list(incorrect_answers))
        user_input = input(f"Which header does '{random_function}' belong to? (enter 'quit' to stop) ")
        if user_input.lower() == 'quit':
            print("Quiz ended.")
            break
        elif user_input == projects[subject][random_function]:
            print("Correct!")
            incorrect_answers.remove(random_function)  # Remove correct answer from the set
        else:
            print(f"Incorrect. The correct answer is '{projects[subject][random_function]}'.")

    if not incorrect_answers:
        print("You have answered all questions correctly for this subject!")

def main():
    parser = argparse.ArgumentParser(description='CLI for memorizing library functions and headers.')
    parser.add_argument('--add', nargs=3, metavar=('FUNCTION', 'HEADER', 'SUBJECT'), help='Add a function and its header to a subject')
    parser.add_argument('--view', nargs='?', const=True, metavar='SUBJECT', help='View all functions and headers, optionally for a specific subject')
    parser.add_argument('--quiz', nargs='?', const=True, metavar='SUBJECT', help='Quiz yourself on functions and headers for a specific subject')

    args = parser.parse_args()

    if args.add:
        add_function(args.add[0], args.add[1], args.add[2])
    elif args.view:
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
                if 0 <= choice < len(subjects):
                    quiz(subjects[choice])
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            quiz(args.quiz)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
