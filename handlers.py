import json
import os

import requests

from constants import TEMP_DIR, AUDD_IO_API_KEY


def handle_message(update, context):
    text = str(update.message.text).lower()
    print("Handle text:", text)
    update.message.reply_text(get_deafult_message())


def get_deafult_message():
    message = "Send me some audio, and I'll name the song for you"
    return message

def handle_voice(update, context):
    print("Handle voice message")
    handle_audio_file(update, context, context.bot.get_file(update.message.voice))


def handle_audio(update, context):
    print("Handle audio message")
    handle_audio_file(update, context, context.bot.get_file(update.message.audio))


def handle_audio_file(update, context, audio):
    chat_id = update.message.from_user['id']
    audio_file = context.bot.get_file(audio.file_id)
    audio_file_path = audio_file.download(os.path.join(TEMP_DIR, audio.file_id + ".mp3"))
    music_json_data = recognize_music_from_file(audio_file_path)
    if music_json_data['result'] is None:
        update.message.reply_text("Music not recognized")
        return

    music = get_music_name(music_json_data)
    image = get_image_by_url(
        music_json_data['result']['deezer']['contributors'][0]['picture_medium'],
        music_json_data['result']['artist'] + ".jpg"
    )
    context.bot.sendPhoto(chat_id=chat_id, photo=open(image, 'rb'), caption=music)

def get_music_name(music_json_data):
    artist = music_json_data['result']['artist']
    title = music_json_data['result']['title']
    album = music_json_data['result']['album']
    return artist + " - " + title + "\nAlbum: " + album

def get_image_by_url(url, filename):
    result = requests.get(url)
    filePath = os.path.join(TEMP_DIR, filename)
    with open(filePath, 'wb') as localFile:
        localFile.write(result.content)
        localFile.close()
    return filePath


def recognize_music_from_file(audio_file_path):
    data = {
        'api_token': AUDD_IO_API_KEY,
        'return': 'deezer'
    }
    files = {
        'file': open(audio_file_path, 'rb'),
    }
    result = requests.post('https://api.audd.io/', data=data, files=files)
    json_text = json.loads(result.text)
    return json_text
