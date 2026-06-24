from telethon import TelegramClient, events

api_id = 33441320
api_hash = "2cd43f4045ce2eecf4a6cc58a1efbc94"
canal_origen = -1001713657731
canal_destino = -1002552882528

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=canal_origen))
async def handler(event):
    await client.forward_messages(canal_destino, event.message)

client.start()
client.run_until_disconnected()
