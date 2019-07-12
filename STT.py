import speech_recognition as sr

def stt():
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print('Listening.....')
	    audio = r.listen(source)
	    print('OK!')
	    
	text = r.recognize_google(audio)
	return(text)

