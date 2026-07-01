# nexus Voice Assistant

nexus is a local voice-controlled desktop assistant built with Python, designed to allow complete hands-free interaction with a computer through voice commands.

The project was created with the idea of enabling users to control their computer while moving, studying, or working without constantly using a keyboard or mouse.

Unlike cloud assistants, nexus focuses on local execution and offline speech recognition.

---

## Main Idea

The original goal of the project is simple:

```text
User speaks
↓
nexus listens
↓
nexus interprets command
↓
nexus executes action locally
```

The long-term vision is creating a lightweight local assistant capable of controlling a computer entirely by voice, even without internet access.

---

## Current Features

Implemented so far:

* Wake word activation (**nexus**)
* Offline speech recognition using Vosk
* Voice recognition in Portuguese
* Text mode for debugging
* Voice mode for real usage
* Continuous dictation mode
* Stop dictation by speaking wake word again
* Open desktop applications through commands
* Execute grouped automation routines
* Multimedia control
* System control commands
* Voice feedback using text-to-speech
* Modular architecture for easy expansion

---

## Example Commands

### Application Control

```text
nexus
abrir opera

nexus
abrir vscode

nexus
abrir calculadora

nexus
abrir bloco de notas
```

### System Commands

```text
nexus
copiar

nexus
colar

nexus
fechar janela
```

### Multimedia Commands

```text
nexus
pausar vídeo

nexus
aumentar volume

nexus
diminuir volume

nexus
mutar
```

### Routines

```text
nexus
modo programação

nexus
modo estudo
```

### Dictation Mode

```text
nexus
modo escrita
```

After activation:

```text
Anything spoken becomes text automatically
```

To stop:

```text
nexus
```

---

## Technologies Used

* Python 3
* Vosk (Offline Speech Recognition)
* PyAudio
* SpeechRecognition
* pyttsx3
* PyAutoGUI
* keyboard
* sounddevice

---

## Project Architecture

```text
voice_assistant/
│
├── main.py
├── config.py
├── router.py
├── matcher.py
├── speaker.py
├── speech_local.py
├── state.py
│
└── commands/
    ├── __init__.py
    ├── apps.py
    ├── media.py
    ├── system.py
    ├── routines.py
    └── dictation.py
```

---

## Development Roadmap

Completed:

* [x] Wake word detection
* [x] Voice recognition
* [x] Offline speech recognition
* [x] Voice feedback
* [x] Desktop application launcher
* [x] Multimedia controls
* [x] Dictation mode
* [x] Modular architecture

Planned:

* [ ] Better continuous listening system
* [ ] Smarter command interpretation
* [ ] Context-based modes
* [ ] Smartphone integration
* [ ] Notebook backpack mode
* [ ] Background execution
* [ ] Faster local speech processing
* [ ] Windows full automation

---

## Future Goal

Transform nexus into a lightweight local operating assistant capable of controlling a computer entirely through voice commands.

Main target use case:

```text
Notebook inside backpack
↓
Headset microphone connected
↓
User walking or moving
↓
Computer fully controlled by voice
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/Jose-FernandoAL/nexus-voice-assistant.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download Vosk Portuguese model separately and place inside:

```text
models/
```

---

## Author

José Fernando Alves Leite

Computer Science Student

GitHub:

https://github.com/Jose-FernandoAL
