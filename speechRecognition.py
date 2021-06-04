import speech_recognition as sr
import gtts as gTTS
import os
import googletrans
from googletrans import Translator

r = sr.Recognizer()

with sr.Microphone() as input_audio:
    print("record")
    speech_text = r.listen(input_audio)

    print("recorded")

    print("Recorded Text : "+r.recognize_google(speech_text))

#print(googletrans.LANGUAGES)

reco_text = r.recognize_google(speech_text)
print("recognized text : "+r.recognize_google(speech_text,language="ml-IN"))

translator = Translator()

t = translator.translate(reco_text,dest="ml")


text_speech = t.text

output = gTTS.gTTS(text=text_speech,lang="ml")
output.save(r"translated.mp3")
os.system(r"translated.mp3")