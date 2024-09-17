from telethon import TelegramClient

api_id = '21061868'
api_hash = 'db1fd0ffbeb954ded8c31da6fc08bfe2'

client = TelegramClient('my_telegram_session', api_id, api_hash)

async def fetch_telegram_messages(keyword):
    await client.start()
    async for message in client.iter_messages('channel_or_group_name'):
        if keyword in message.text:
            print(message.text)
