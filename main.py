import requests
from work import *

filename = "abcd.wav"
audio_url = upload(filename)

save_transcript(audio_url, 'file_title')