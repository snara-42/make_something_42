import random
import time

from colorama import Fore, Style
import colorama


def draw_fortune(category):
    fortunes = {
        "career": [
            "You will debug a tough issue successfully. 🛠️",
            "A new framework will make your life easier. 🚀",
            "Your hard work will lead to a big promotion. 📈",
            "You will receive an unexpected reward for your project. 🎉"
        ],
        "code quality": [
            "Your code will run perfectly on the first try. ✅",
            "You will find an elegant solution to a complex problem. 💡",
            "An old bug will finally be resolved. 🐛",
            "Your next project will be a huge success. 🌟"
        ],
        "teamwork": [
            "A colleague will praise your coding skills. 👍",
            "You will make a new valuable connection in the industry. 🌐",
            "Your team will achieve a major milestone. 🏆",
            "You will inspire a junior developer. 🌱"
        ],
        "learning": [
            "You will learn a new programming language effortlessly. 📚",
            "A tutorial will help you master a new skill quickly. 🎓",
            "You will discover a powerful new tool. 🔧",
            "Your curiosity will lead to an exciting discovery. 🔍"
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
    import pygame
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
    # play_sound_effect()
    display_ascii_art()

    fortune = draw_fortune(category)
    print(Fore.GREEN + Style.BRIGHT + "Your developer fortune: " + fortune)


if __name__ == "__main__":
    colorama.init(autoreset=True)
    main()
