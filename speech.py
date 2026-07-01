import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True


def preparar_microfone(source):
    print("Calibrando microfone...")
    recognizer.adjust_for_ambient_noise(source, duration=2)


def ouvir(source, tempo=3):
    try:
        audio = recognizer.listen(source, phrase_time_limit=tempo)
        texto = recognizer.recognize_google(audio, language="pt-BR")
        return texto.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        print("Erro no reconhecimento de voz.")
        return ""