import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 150)  
engine.setProperty('volume', 1.0) 


engine.say('hola mundo')
engine.runAndWait()
engine.endLoop()