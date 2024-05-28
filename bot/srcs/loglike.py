from fortune_drawer import draw_fortune


class LogLike:
    def __init__(self):
        self.condition = None
        self.level = 0
        self.program_condition = {
            '0': {
                '1': ['1.start the game'],
                '2': ['2.exit'],
            },
            '1': {
                '1': [
                    '1. **Read the signboard next to the torii gate**',
                    """
                    **Read the signboard next to the torii gate**
                    You decide to read the signboard next to the torii gate. The wooden board is engraved with elegant Japanese characters, and an English translation is provided for international visitors. It reads:
                    "Welcome to Denden-gu, the Shrine of Electricity and Radio Waves. Here, professionals from the electrical and telecommunications industries seek blessings for the smooth operation of their systems. Visitors may pray for the resolution of computer and smartphone issues and the development of technology."
                    The signboard also mentions the history of the shrine, including its destruction by fire and reconstruction in 1969. It invites you to explore the shrine and draw a special omikuji, a fortune slip designed specifically for software developers.
                    """, 
                ],
                '2': ['2. explore the surrounding area of the shrine.', 
                      """
                      **explore the surrounding area of the shrine.**
                        You decide to explore the surrounding area of the shrine. As you walk around, you notice several interesting features:
                        To your left, there is a small garden with carefully raked gravel and stone lanterns, offering a peaceful spot to reflect and enjoy the beauty of the shrine. The garden also has reliefs of Edison and Hertz, paying homage to pioneers of electricity and radio waves.
                        To your right, you see a small wooden pavilion where visitors can sit and rest. On a nearby table, there are SD card amulets for sale, each said to bring good luck and protection to your electronic devices.
                        Further ahead, you spot a path leading deeper into the forest, inviting you to take a stroll through the natural beauty surrounding the shrine
                      """],
                '3': ['3. **Proceed to the main shrine area to make an offering and draw a fortune slip**',
                      """
                      **Proceed to the main shrine area to make an offering and draw a fortune slip**
                      You reach the offering box, a large wooden structure with a slotted top. Nearby, there is a stand with neatly arranged omikuji, fortune slips specifically designed for software developers. A sign next to the stand explains that these fortunes can offer guidance and blessings for various aspects of software development, from debugging to system stability.
                      You take a moment to make a small offering, bow, and clap your hands twice in prayer. After your prayer, you pick up an omikuji from the stand.
                      """
                      ],
                '4': ['4. **Leave the shrine**', "exit"],
            },
        }

    def play(self):
        previous_select: int | None = None
        condition = self.program_condition[str(self.level)]
        while True:
            try:
                if previous_select:
                    print(condition[previous_select][1])
                    if previous_select == '3':
                        data = draw_fortune('career')
                        print('========================================')
                        print(data)
                        print('========================================')
                for _, v in condition.items():
                    print(v[0])
                user_input = input('Enter press key: ')
                if int(user_input) == len(condition):
                    break
                if self.level == 0 and '1' <= user_input <= '2':
                    self.level = 1
                elif self.level == 1:
                    previous_select = user_input
                condition = self.program_condition[str(self.level)]

            except Exception as e:
                print(e)

                
if __name__ == "__main__":
    loglike = LogLike()
    loglike.play()
