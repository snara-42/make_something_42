import argparse

# Dictionary to store functions and headers
function_headers = {
    'printf': 'stdio.h',
    'malloc': 'stdlib.h',
    'strcpy': 'string.h',
    # Add more functions and headers as needed
}

def add_function(function, header):
    function_headers[function] = header
    print(f"Added: {function} -> {header}")

def view_functions():
    for function, header in function_headers.items():
        print(f"{function} -> {header}")

def quiz():
    import random
    functions = list(function_headers.keys())
    random_function = random.choice(functions)
    user_input = input(f"Which header does '{random_function}' belong to? ")
    if user_input == function_headers[random_function]:
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
