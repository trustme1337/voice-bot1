from aiogram import types
from utils.history import add_to_history
from aiogram.types import FSInputFile
from gtts import gTTS
import os

async def handle_text(message: types.Message):
    # Сохраняем текст в историю
    add_to_history(message.from_user.id, message.text)

    # Генерация голоса с помощью Google TTS
    tts = gTTS(text=message.text, lang="ru")
    audio_file_path = f"voice_{message.from_user.id}.mp3"
    tts.save(audio_file_path)

    # Отправляем голосовое сообщение
    voice_file = FSInputFile(audio_file_path)
    await message.answer_voice(voice_file)

    # Удаляем временный файл
    os.remove(audio_file_path)

def register_handlers(dp):
    dp.message.register(handle_text)
