import random


def fortune():
    unlucky = [
        "segmentation fault", "norme error", "bus error", "double free",
        "uninitialized variables", "overflow", "memory leak"
    ]
    lucky = ["everything", "your teamwork", "exam", "lunch", "debugging"]
    msg = f"today beware of {random.choice(unlucky)}, but {random.choice(lucky)} shall go well!"
    print(msg)

if __name__ == "__main__":
    fortune()
