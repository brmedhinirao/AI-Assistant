import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr

api_key = "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"

lang = 'en'

openai.api_key = api_key

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)

                if "Friday" in said:
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", message=[{"role": "user", "content": said}])
                    text = completion.choices[0].message.content
                    speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                    speech.save("welcome1.mp3")
                    playsound.playsound("welcome1.mp3")

            except Exception:
                print("Exception")

        return said

    get_audio()






