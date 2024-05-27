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

# Flatten the projects dictionary into function_headers
function_headers = {func: header for project in projects.values() for func, header in project.items()}

def add_function(function, header):
    function_headers[function] = header
    print(f"Added: {function} -> {header}")

def view_functions():
    for function, header in function_headers.items():
        print(f"{function} -> {header}")

def quiz():
    functions = list(function_headers.keys())
    while True:
        random_function = random.choice(functions)
        user_input = input(f"Which header does '{random_function}' belong to? (enter 'quit' to stop) ")
        if user_input.lower() == 'quit':
            print("Quiz ended.")
            break
        elif user_input == function_headers[random_function]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is '{function_headers[random_function]}'.")

def main():
    parser = argparse.ArgumentParser(description='CLI for memorizing library functions and headers.')
    parser.add_argument('--add', nargs=2, metavar=('FUNCTION', 'HEADER'), help='Add a function and its header')
    parser.add_argument('--view', action='store_true', help='View all functions and headers')
    parser.add_argument('--quiz', action='store_true', help='Quiz yourself on functions and headers')

    args = parser.parse_args()

    if args.add:
        add_function(args.add[0], args.add[1])
    elif args.view:
        view_functions()
    elif args.quiz:
        quiz()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
