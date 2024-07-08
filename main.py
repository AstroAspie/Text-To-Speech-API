from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from gtts import gTTS
import os

from fastapi import FastAPI

app = FastAPI()


tmp_file_dir = "/"
Path(tmp_file_dir).mkdir(parents=True, exist_ok=True)


def text_to_speech(textIn, language="en"):
    myobj = gTTS(text=textIn, lang=language, slow=False)
    filepath = "saved.mp3"
    myobj.save(filepath)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/convert/{textString}")
async def convert_text_to_speech(textString):
    text_to_speech(textString)
    with open(os.path.join(tmp_file_dir, "saved.mp3"), "rb") as disk_file:
        disk_file.read()
        # os.system("rm saved.mp3")
        return FileResponse("saved.mp3", media_type="audio/mpeg")
