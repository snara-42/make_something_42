#!python3

import random


def fortune():
    unlucky = [
        "segmentation fault", "norme error", "bus error", "double free", "infinite loop",
        "uninitialized variables", "overflow", "memory leak", "overwork", "undefined behavior",
        "TIG", "stumbling on cables", "running out of memory", "getting lost on the way home",
    ]
    lucky = [
        "everything else", "your teamwork", "taking a nap", "lunch time", "finding a new friend",
        "debugging", "review", "exam", "hackathon", "preprocessing", "compiling", "linking",
        "resolving issues", "resolving conflicts", "learing a language", "allocating memory",
    ]
    msg = f"Today thou shalt beware of {random.choice(unlucky)}, but {random.choice(lucky)} shall go well with thee!"
    print(msg)


if __name__ == "__main__":
    fortune()
