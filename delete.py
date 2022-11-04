from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon import errors

phone = input('Enter your phone number: ')
api_id = input('Go to https://my.telegram.org/apps, sign in, go to API development tools, create an app \nEnter api_id: ')
api_hash = input('Enter api_hash: ')

client = TelegramClient(phone, api_id, api_hash)


client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))
    except errors.SessionPasswordNeededError:
        client.sign_in(password=input('Enter password: '))


dialogs = client.get_dialogs()


for dialog in dialogs:
    try:
        client.delete_dialog(dialog)
    except:
        continue
