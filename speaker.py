import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 180)
engine.setProperty("volume", 1.0)


def falar(texto):
    print(f"Tatsu: {texto}")
    engine.say(texto)
    engine.runAndWait()