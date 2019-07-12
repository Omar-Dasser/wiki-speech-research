import STT
import requests
from bs4 import BeautifulSoup
import tts
query = STT.stt()
#query = 'Google'
print("Serching from Wikipedia for "+query+" .....")

url = "https://www.wikipedia.org/wiki/"+query

#print("*****************")
response = requests.get(url)

#print(response)

soup = BeautifulSoup(response.text,"html.parser")

#print(soup)
#print("*****************************************************************")
i = 0
for p in soup.find_all("p"):
	#print("*****")
	if(i == 2):
		text = p.get_text()
		print(text)
		tts.TTS(text)
		tts.play()
	i = i+1