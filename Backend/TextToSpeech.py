<<<<<<< HEAD
pass
=======
import pygame
import random
import asyncio
import edge_tts
import os
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
AssistantVoice = env_vars.get("AssistantVoice")

async def TextToAudioFile(text) -> None:
    communicate = edge_tts.Communicate(text, voice=AssistantVoice)
    await communicate.save("Data/Audio.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("Data/Audio.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(1)
>>>>>>> ab02c4ad3a1c9dc10eba305312a7edd41519101f
