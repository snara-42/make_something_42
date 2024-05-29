import time
from fortune_drawer import draw_fortune


class Roguelike:
    def __init__(self):
        self.condition = None
        self.level = 0
        self.previous_select = None
        self.program_condition = {
            '0': {
                '1': [
                    'Start the game',
                    """
You arrive at the entrance of Hōrin-ji Temple in Arashiyama, Kyoto. The path leading to the shrine is lined with tall bamboo and cherry blossom trees, creating a serene and picturesque atmosphere. As you walk closer, you see the vibrant red torii gate marking the entrance to "Denden-gu.”
                    """
                ],
                '2': ['Exit', 'exit'],
            },
            '1': {
                '1': [
                    'Read the signboard next to the torii gate',
                    """
You decide to read the signboard next to the torii gate. The wooden board is engraved with elegant Japanese characters, and an English translation is provided for international visitors. It reads:
"Welcome to Denden-gu, the Shrine of Electricity and Radio Waves. Here, professionals from the electrical and telecommunications industries seek blessings for the smooth operation of their systems. Visitors may pray for the resolution of computer and smartphone issues and the development of technology."
The signboard also mentions the history of the shrine, including its destruction by fire and reconstruction in 1969. It invites you to explore the shrine and draw a special omikuji, a fortune slip designed specifically for software developers.
                    """,
                ],
                '2': [
                    'Explore the surrounding area of the shrine.',
                    """
The surrounding area of the shrine is serene and filled with the sound of nature. You see a few visitors wandering around, admiring the beauty of the place. There's a small garden with meticulously maintained plants and a koi pond. The atmosphere is peaceful and calming, perfect for contemplation.
                    """,
                ],
                '3': [
                    'Proceed to the main shrine area to make an offering and draw a fortune slip',
                    """
You reach the offering box, a large wooden structure with a slotted top. Nearby, there is a stand with neatly arranged omikuji, fortune slips specifically designed for software developers. A sign next to the stand explains that these fortunes can offer guidance and blessings for various aspects of software development, from debugging to system stability.
You take a moment to make a small offering, bow, and clap your hands twice in prayer. After your prayer, you pick up an omikuji from the stand.
                    """,
                ],
                '4': ['Leave the shrine', "exit"],
            },
        }

    def animated_drawing_effect(self):
        print("Drawing your fortune", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        print("\n")

    def display_menu(self):
        condition = self.program_condition[str(self.level)]
        for key, value in condition.items():
            print(f"{key}. {value[0]}")

    def handle_input(self, user_input):
        condition = self.program_condition[str(self.level)]
        if user_input not in condition:
            print("Invalid input, please try again.")
            return False

        if self.level == 0 and user_input in ['1', '2']:
            print(condition[user_input][1])  # Print introductory text
            self.level = 1
        elif self.level == 1:
            self.previous_select = user_input
            if user_input == '4':
                return True

            print(condition[user_input][1])
            if user_input == '3':
                self.animated_drawing_effect()
                data = draw_fortune()
                print('========================================')
                print(data)
                print('========================================')

        return False

    def play(self):
        while True:
            try:
                if self.previous_select:
                    pass  # Previously selected option's output is already handled in handle_input

                self.display_menu()
                user_input = input('Enter choice: ')
                if self.handle_input(user_input):
                    break

            except Exception as e:
                print(e)


if __name__ == "__main__":
    roguelike = Roguelike()
    roguelike.play()
