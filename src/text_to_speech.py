import pyttsx3

#convert text to speech for assistant 
def speak(text):
    engine = pyttsx3.init(driverName="sapi5")
    engine.setProperty("rate", 165)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.say(text)
    engine.runAndWait()