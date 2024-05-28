from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from response import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


async def send_message(message: Message, umessage: str) -> None:
    if not umessage:
        return
    if is_private := umessage[0] == '?':
        umessage = umessage[1:]
    if umessage[0] == '#':
        umessage = umessage[1:]
    else:
        return
    try:
        response: str = get_response(umessage, is_private)
        await message.author.send(response) if is_private else await \
            message.channel.send(response)
    except Exception as e:
        print(e)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    await send_message(message, message.content)


def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
