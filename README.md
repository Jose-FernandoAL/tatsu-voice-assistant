# Tatsu Voice Assistant

Tatsu is a local voice-controlled assistant developed in Python for hands-free computer interaction.

The project was created with the goal of allowing users to control a computer using voice commands, reducing the need for direct interaction with keyboard or mouse and enabling more practical usage while moving or performing other activities.

## Features

Current implemented functionalities:

* Custom wake word activation (**Tatsu**)
* Voice recognition with microphone input
* Text mode for debugging and testing
* Open desktop applications through commands
* Execute grouped routines (study mode, programming mode)
* Multimedia controls
* Basic system controls
* Voice feedback using text-to-speech
* Modular architecture for easy expansion

## Example Commands

```text
Tatsu
abrir opera

Tatsu
modo programação

Tatsu
aumentar volume

Tatsu
pausar vídeo
```

## Technologies Used

* Python 3
* SpeechRecognition
* PyAudio
* PyAutoGUI
* keyboard
* pyttsx3

## Project Structure

```text
voice_assistant/
│
├── main.py
├── config.py
├── speech.py
├── speaker.py
├── router.py
├── matcher.py
├── state.py
│
└── commands/
    ├── apps.py
    ├── media.py
    ├── routines.py
    └── system.py
```

## Roadmap

Completed:

* [x] Wake word detection
* [x] Voice recognition
* [x] Desktop application launcher
* [x] Multimedia controls
* [x] Voice feedback
* [x] Modular command architecture

Planned:

* [ ] Fully offline speech recognition
* [ ] Voice dictation mode
* [ ] Context-based command system
* [ ] Notebook backpack mode
* [ ] Smartphone integration
* [ ] Advanced automation workflows

## Purpose

The main objective of Tatsu is to become a lightweight local assistant capable of controlling a computer entirely by voice commands, focusing on accessibility, productivity, and hands-free interaction.

## Author

José Fernando Alves Leite

GitHub: https://github.com/Jose-FernandoAL
