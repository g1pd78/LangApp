from fastapi import FastAPI
import requests	
from bs4 import BeautifulSoup

s = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=API-ключ&lang=en-ru&text=time"

def search(key):

	defaultLang = 'russian'
	langList = ['english']
	word = "time"
	#req = requests.get(f"https://dictionary.yandex.net/api/v1/dicservice.json/getLangs?key={args.key}")
	#req = requests.get(f"https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={args.key}&lang=ru-ru&text={word}")
	#print(req.json())
	for language in langList:
		headers = {'User-Agent': 'Mozilla/5.0'}
		#payload = f"https://context.reverso.net/translation/{defaultLang}-{language}/{word}"
		resp1 = requests.get(f"https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={key}&lang=en-ru&text={word}")
		#response = requests.get(f"http://context.reverso.net/translation/{defaultLang}-{language}/{word}", headers=headers)
		print(resp1.json())
		

#app = FastAPI()
#@app.get("/")














