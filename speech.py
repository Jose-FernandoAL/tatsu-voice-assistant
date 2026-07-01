import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True


def preparar_microfone(source):
    print("Calibrando microfone...")
    recognizer.adjust_for_ambient_noise(source, duration=2)

def ouvir_continuo(source):
    try:
        audio = recognizer.listen(source)   # sem limite

        texto = recognizer.recognize_google(
            audio,
            language="pt-BR"
        )

        return texto.lower()

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        print("Erro reconhecimento")
        return ""
    
