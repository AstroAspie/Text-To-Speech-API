# from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from gtts import gTTS
# Create your views here.


def text_to_speech(textIn, language="en"):
    myobj = gTTS(text=textIn, lang=language, slow=False)
    filepath = "saved.mp3"
    myobj.save(filepath)


def convertTextToSpeech(request, text):
    text_to_speech(text)
    try:
        file = open("saved.mp3", 'rb')
        res = FileResponse(file)
        res['Content-Type'] = 'audio/mpeg'
        return res
    except FileNotFoundError:
        return HttpResponse("File not found", status=404)
