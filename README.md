# Audio Transcriber

A beginner-friendly Python tool that converts audio files into text using OpenAI's Whisper model. Perfect for those who want to start their journey in audio processing!

## What Does This Tool Do?

This tool helps you convert spoken words from audio files into written text. It's like having a super-smart assistant that listens to audio and writes down everything it hears!

## Key Features

- 🎵 Works with common audio formats (MP3, WAV, M4A)
- 🎯 High accuracy in converting speech to text
- 🌍 Supports multiple languages
- 💻 Simple command line interface (don't worry, we'll explain how to use it!)
- 🔒 Clean project setup with virtual environment (we'll explain what this means)

## Before You Start (Prerequisites)

1. **Python**: You need Python 3.x installed on your computer
   - Not sure if you have Python? Open your terminal/command prompt and type: `python --version`
   - If you don't have Python, download it from [Python's official website](https://www.python.org/downloads/)

2. **pip**: The Python package installer (usually comes with Python)
   - To check if you have pip, run: `pip --version`

## Step-by-Step Installation Guide

1. **Download the Project**
   ```bash
   # Clone this repository (copy all the files to your computer)
   git clone <repository-url>
   
   # Go into the project folder
   cd transcriber
   ```

2. **Set Up a Virtual Environment** (like a clean room for your project)
   ```bash
   # Create a virtual environment named 'venv'
   python -m venv venv
   
   # Activate the virtual environment:
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
   
   After activation, you should see `(venv)` at the beginning of your terminal line

3. **Install Required Packages**
   ```bash
   # Install all the tools this project needs
   pip install -r requirements.txt
   ```

## How to Use

1. **Basic Usage**
   ```bash
   # Format:
   python transcribe.py <path-to-your-audio-file>
   
   # Example:
   python transcribe.py my_recording.mp3
   ```

2. **Real Examples**
   ```bash
   # Transcribe an MP3 file
   python transcribe.py audio/interview.mp3
   
   # Transcribe a WAV file
   python transcribe.py audio/lecture.wav
   
   # Transcribe an M4A file
   python transcribe.py audio/voice_note.m4a
   ```

## Supported Audio Formats

- **MP3** (.mp3) - Most common audio format
- **WAV** (.wav) - High-quality audio format
- **M4A** (.m4a) - Common format for voice recordings

## Project Structure Explained

```
transcriber/
├── transcribe.py     # The main program that does the transcription
├── requirements.txt  # List of required Python packages
└── README.md        # This help file you're reading now
```

## Troubleshooting Common Issues

1. **"Command not found: python"**
   - Make sure Python is installed and added to your system's PATH
   - Try using `python3` instead of `python`

2. **"No module named 'whisper'"**
   - Make sure you activated the virtual environment
   - Try reinstalling requirements: `pip install -r requirements.txt`

3. **"Audio file not found"**
   - Check if the audio file path is correct
   - Make sure you're in the right directory
   - Use the full path to the audio file if needed

4. **Virtual Environment Issues**
   - If `venv` command not found: `python -m pip install virtualenv`
   - If activation fails, check if you're in the project directory

## Key Terms Explained

- **Virtual Environment**: A clean, isolated space for your Python project
- **pip**: Python's package installer - helps you add tools to your project
- **Command Line**: The text interface where you type commands
- **Repository**: The project's folder with all its files
- **PATH**: A system setting that helps your computer find programs

## Development Tips for Beginners

1. Always activate your virtual environment before working
2. Keep your Python and packages updated
3. Check error messages carefully - they often tell you what's wrong
4. Save audio files in supported formats (MP3, WAV, M4A)

## Contributing

New to coding? You can still contribute!
1. Report bugs (things that don't work)
2. Suggest improvements
3. Help improve this documentation
4. Share your experience using the tool

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Need Help?

If you're stuck:
1. Read the error message carefully
2. Check the troubleshooting section above
3. Make sure you followed all steps in order
4. Search for the error message online
5. Ask for help in the project's issues section

Happy Transcribing! 🎉