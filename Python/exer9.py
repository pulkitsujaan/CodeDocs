import json
import requests
def speaker(str):
    from win32com.client import Dispatch
    speak= Dispatch("SAPI.SpVoice")
    speak.Speak(str)
speaker("Today's news headlines are...")
url="http://newsapi.org/v2/top-headlines?country=in&apiKey=0944e494429248bdb33d62b01011d1da"
news=requests.get(url).text
py_news=json.loads(news)
headline=py_news["articles"]
for news in headline:
    speaker(news["title"])
    if news==headline[len(headline)-1]:
        break
    else:
        speaker("Moving to the next headline...")