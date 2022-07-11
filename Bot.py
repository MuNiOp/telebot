import asyncio
from random import choice

from telethon import TelegramClient
from telethon.events import NewMessage

APP_ID = 1252636
API_HASH = '4037e9f957f6f17d461b0c288ffa50f1'

HEART = 'ты'
COLORED_HEARTS = [' гей?', ' топ?', ' любишь парней?', ' абоба?', ' любишь девушек?', ' паришь?', ' автобус?']
MAGIC_PHRASES = ['слить']
EDIT_DELAY = 1.20

PARADE_MAP = '''
0110
0110
0110
'''

client = TelegramClient('tg-account', APP_ID, API_HASH)


def generate_parade_colored():
    output = ''
    for c in PARADE_MAP:
        if c == '0':
            output += HEART
        elif c == '1':
            output += choice(COLORED_HEARTS)
        else:
            output += c
    return output


async def process_love_words(event: NewMessage.Event):
    await client.edit_message(event.peer_id.user_id, event.message.id, 'ты топ?')
    await asyncio.sleep(4)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'ты гей?')
    await asyncio.sleep(4)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'ты молодец?')
    await asyncio.sleep(4)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'ты любишь парней?')
    await asyncio.sleep(4)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'ты гетеро?')
    await asyncio.sleep(4)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'ты абоба?')
    await asyncio.sleep(4)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'хз что писать?')
    await asyncio.sleep(4)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'и тут хз')
    await asyncio.sleep(4)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'я немой💗')
    await asyncio.sleep(4)


async def process_build_place(event: NewMessage.Event):
    output = ''
    for i in range(8):
        output += '\n'
        for j in range(11):
            output += HEART
            await client.edit_message(event.peer_id.user_id, event.message.id, output)
            await asyncio.sleep(EDIT_DELAY / 2)


async def process_colored_parade(event: NewMessage.Event):
    for i in range(50):
        text = generate_parade_colored()
        await client.edit_message(event.peer_id.user_id, event.message.id, text)

        await asyncio.sleep(EDIT_DELAY)


@client.on(NewMessage(outgoing=True))
async def handle_message(event: NewMessage.Event):
    if event.message.message in MAGIC_PHRASES:
        await process_build_place(event)
        await process_colored_parade(event)
        await process_love_words(event)
        


if __name__ == '__main__':
    print('[*] Даа')
    client.start()
    client.run_until_disconnected()
