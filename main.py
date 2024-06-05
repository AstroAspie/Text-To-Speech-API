from gtts import gTTS

import os

# myText = 'Welcome Home'
myText = open("textfile.txt", "r")

language = 'en'

myobj = gTTS(text=myText.read(), lang=language, slow=False)
myobj.save("welcome.mp3")
# os.system("start welcome.mp3")
os.system("afplay welcome.mp3")
