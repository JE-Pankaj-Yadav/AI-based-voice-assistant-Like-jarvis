# AI-based-voice-assistant-Like-jarvis
An AI-based voice assistant, like Jarvis, is like having a smart friend in your device. It listens to your voice and helps you with things, just like talking to a buddy. Imagine asking it to set a reminder, play your favorite music, or even tell you a joke!
<br>

# AI Voice Assistant - Jarvis-like Assistant


## Overview

This AI-based voice assistant is designed to function like a personal digital assistant, similar to Jarvis from Iron Man. It can perform a wide range of tasks through voice commands, including opening applications, searching the web, managing contacts, checking weather, controlling system functions, and much more. The assistant features a graphical user interface (GUI) for visual feedback and interaction.


## 📑 Table of Contents

- [✨ Features](#-features)
- [🧰 Tools & Technologies Used](#-tools--technologies-used)
- [📁 Project Files](#-project-files)
- [⚙️ How to Use (Setup)](#️-how-to-use-setup)
- [📹 Demo (Coming Soon)](#-demo-coming-soon)
- [📝 Notes](#-notes)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [👨‍💻 Developer Info](#-developer-info)
- [⭐ Support](#-support)

---

# ✨ Features

### Core Functionalities
- **Voice Recognition**: Listens and responds to voice commands using speech recognition
- **Text-to-Speech**: Provides audible responses using text-to-speech synthesis
- **Multi-tasking**: Capable of handling various tasks simultaneously

### System Control
- Open/close applications
- System monitoring (battery, CPU usage)
- System power management (shutdown, restart, sleep)
- Volume control
- Screenshot capture
- WiFi password retrieval

### Information Services
- Weather forecasts
- Internet speed testing
- IP address information
- Location tracking
- Wikipedia searches
- News updates
- Time and date information

### Communication Tools
- WhatsApp message sending
- Email functionality
- Contact management (add, display contacts)
- Phone number tracking/location

### Entertainment
- Music playback
- Joke telling
- Interactive conversations

### Productivity Tools
- PDF reading
- Remembering notes/tasks
- Shopping site access
- Social media integration (Instagram profile access)

## Technical Specifications

### Technologies Used
- Python 3.x
- PyQt5 for GUI
- SpeechRecognition library
- pyttsx3 for text-to-speech
- OpenAI API for advanced queries
- Various system and web APIs

### Requirements
- Windows operating system
- Python 3.x installed
- Required Python packages (listed in requirements.txt)
- Internet connection for certain features
- Microphone for voice input

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pankajyadavup53/AI-based-voice-assistant-Like-jarvis.git
   cd AI-based-voice-assistant-Like-jarvis
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key in `apikey.py`

4. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. Launch the application
2. Click the "START" button on the GUI
3. Speak commands clearly when prompted
4. The assistant will respond verbally and display information on the GUI

### Example Commands
- "What's the weather today?"
- "Open Chrome"
- "What's my IP address?"
- "Tell me a joke"
- "Send a WhatsApp message"
- "What's the time?"
- "Shutdown the system"

## Project Structure

```
AI-based-voice-assistant-Like-jarvis/
├── apikey.py                # API key configuration
├── application.py           # Application management functions
├── Contacts.txt             # Contact storage
├── Display.py               # Display and system monitoring functions
├── keyboard.py              # Keyboard input functions
├── main.py                  # Main application logic
├── PhoneNumer.py            # Phone number tracking functions
├── remember_data.txt        # Reminder storage
├── VA_GUI.py                # GUI implementation
└── images/                  # GUI assets
```

## Known Limitations

- Primarily designed for Windows systems
- Some features require internet connectivity
- Voice recognition accuracy may vary based on microphone quality
- Certain system-specific paths may need adjustment for different environments

## Future Enhancements

- Cross-platform compatibility
- Enhanced natural language processing
- More integration with smart home devices
- Machine learning for personalized responses
- Mobile app version

## License

This project is open-source and available for personal and educational use. For commercial use, please contact the author.

---

**Author**: Pankaj Yadav (JE-Pankaj-yadav)  
**Contact**: For questions or contributions, please open an issue on the GitHub repository.