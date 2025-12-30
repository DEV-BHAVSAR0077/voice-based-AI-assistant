import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1.5          # check the silence between word
recognizer.dynamic_energy_threshold = True

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = recognizer.listen(
            source,
            timeout=None,                 # wait for user speaking 
            phrase_time_limit=5          #give the respose after 5 sec silence by user 
        )

    try:
        text = recognizer.recognize_google(audio)
        print("User said:", text)
        return text.strip()
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None