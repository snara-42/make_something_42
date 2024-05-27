#!python3

import random


def fortune():
    unlucky = [
        "segmentation fault", "norme error", "bus error", "double free", "infinite loop",
        "uninitialized variables", "overflow", "memory leak", "overwork",
        "TIG", "stumbling on a cable", "running out of memory",
    ]
    lucky = [
        "everything", "your teamwork", "exam", "lunch", "debugging", "review", "nap",
    ]
    msg = f"today beware of {random.choice(unlucky)}, but {random.choice(lucky)} shall go well!"
    print(msg)


if __name__ == "__main__":
    fortune()
