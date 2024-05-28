from fortune_drawer import draw_fortune, category_show

"""

    not yet save high score quiz
    show quiz result

"""


def get_response(message: str, is_private: bool = False) -> str:
    if "get score" in message:
        return "get high score in database"
    elif "fortune" in message and is_private:
        """
        this will be added more
        will be loglike text adventure
        """
        try:
            msg_spt = message.split()
            if len(msg_spt) == 1:
                raise IndexError
            fortune = ' '.join(message.split()[1:]).rstrip()
            if fortune:
                return draw_fortune(fortune)
        except IndexError:
            return category_show()
    elif "quiz" in message:
        return "show quiz result"
    else:
        """
        this will be added more
        """
        return "none"
