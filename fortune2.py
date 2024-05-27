import random
import time
import sys

try:
    from colorama import init, Fore, Style
    import pygame
except ImportError:
    print("Please install required modules: colorama, pygame")
    sys.exit(1)

# Initialize colorama and pygame mixer
init(autoreset=True)
pygame.mixer.init()


def draw_fortune(category):
    fortunes = {
        "career": [
            "You will debug a tough issue successfully. :tools:",
            "A new framework will make your life easier. :rocket:",
            "Your hard work will lead to a big promotion. :chart_with_upwards_trend:",
            "You will receive an unexpected reward for your project. :tada:"
        ],
        "code quality": [
            "Your code will run perfectly on the first try. :white_check_mark:",
            "You will find an elegant solution to a complex problem. :bulb:",
            "An old bug will finally be resolved. :bug:",
            "Your next project will be a huge success. :star2:"
        ],
        "teamwork": [
            "A colleague will praise your coding skills. :thumbsup:",
            "You will make a new valuable connection in the industry. :globe_with_meridians:",
            "Your team will achieve a major milestone. :trophy:",
            "You will inspire a junior developer. :seedling:"
        ],
        "learning": [
            "You will learn a new programming language effortlessly. :books:",
            "A tutorial will help you master a new skill quickly. :mortar_board:",
            "You will discover a powerful new tool. :wrench:",
            "Your curiosity will lead to an exciting discovery. :mag:"
        ]
    }
    return random.choice(fortunes[category])


def animated_drawing_effect():
    print("Drawing your fortune", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(1)
    print("\n")


def show_progress_bar(duration=3):
    print("Drawing progress: [", end="", flush=True)
    for _ in range(duration * 10):
        print("#", end="", flush=True)
        time.sleep(0.1)
    print("]")


def play_sound_effect():
    pygame.mixer.music.load("ding.mp3")
    pygame.mixer.music.play()


def display_ascii_art():
    art = """
    /\\     /\\
   {  `---'  }
   {  O   O  }
    ~~>  V  <~~
     \\ \\|/ /
      `-----'____
      /     \\    \\_
     {       }\\  )_\\_   _
     |  \\_/  ) / / \\_\\_/ )
      \\__/  /(_/  \\__/(_/
           /|
           | \\
    """
    print(Fore.CYAN + art)


def main():
    print("Choose a category for your fortune:")
    print("1. Career")
    print("2. Code Quality")
    print("3. Teamwork")
    print("4. Learning")

    choice = input("Enter the number of your choice: ")
    categories = {
        "1": "career",
        "2": "code quality",
        "3": "teamwork",
        "4": "learning"
    }

    category = categories.get(choice, "career")

    animated_drawing_effect()
    show_progress_bar()
    #play_sound_effect()
    display_ascii_art()

    fortune = draw_fortune(category)
    print(Fore.GREEN + Style.BRIGHT + "Your developer fortune: " + fortune)

if __name__ == "__main__":
    main()
