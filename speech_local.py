import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer


MODEL_PATH = r"models\vosk-model-small-pt"

audio_queue = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(status)
    audio_queue.put(bytes(indata))


model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)


def ouvir_local():
    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=callback
    ):
        print("Ouvindo offline...")

        while True:
            data = audio_queue.get()

            if recognizer.AcceptWaveform(data):
                resultado = json.loads(recognizer.Result())
                texto = resultado.get("text", "").lower()

                if texto:
                    return texto