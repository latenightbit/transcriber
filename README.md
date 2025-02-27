# Audio Transcriber

A Python tool that converts audio files into text using the Faster Whisper model (large-v2). This implementation uses CPU-based inference optimized for general use.

## What Does This Tool Do?

This tool transcribes audio files into text using the Faster Whisper model, an efficient implementation of OpenAI's Whisper model.

## Key Features

- 🎵 Works with common audio formats (MP3, WAV, M4A)
- 🎯 Uses the large-v2 model for high accuracy
- 🌍 Supports multiple languages with automatic language detection
- 💻 Simple command-line interface
- 🚀 Optimized for CPU usage with INT8 quantization

## System Requirements

1. **Python**: Python 3.12 (recommended)
   - Check version: `python3 --version`
   - Download from [Python's official website](https://www.python.org/downloads/) or install via Homebrew on macOS

2. **Hardware**:
   - Sufficient RAM (recommended: 8GB+)
   - Adequate disk space for the model (~4GB for large-v2)
   - CPU with good single-thread performance

3. **Operating System**:
   - Tested on macOS; should work on Linux and Windows with minor adjustments

4. **Dependencies**:
   - FFmpeg (required by the `av` library for audio processing)

## Installation Guide

Follow these steps to set up the tool from scratch:

1. **Install Python 3.12**
   - **macOS**:
     ```bash
     brew install python@3.12
     ```
   - **Linux**: Use your package manager (e.g., `sudo apt-get install python3.12` on Ubuntu, if available) or compile from source.
   - **Windows**: Download from [python.org](https://www.python.org/downloads/) and install, ensuring it’s added to PATH.
   - Verify:
     ```bash
     python3.12 --version
     ```
     - **Note**: Python 3.13 is not recommended due to compatibility issues with the `av` dependency. Use Python 3.12.

2. **Install System Dependencies**
   - **FFmpeg** (needed for audio processing):
     - **macOS**:
       ```bash
       brew install ffmpeg
       ```
     - **Linux** (Ubuntu/Debian):
       ```bash
       sudo apt-get install ffmpeg
       ```
     - **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html), extract, and add the `bin` folder to your system PATH.
     - Verify:
       ```bash
       ffmpeg -version
       ```

3. **Download the Project**
   ```bash
   git clone <repository-url>
   cd transcriber
   ```

4. **Set Up a Virtual Environment**
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   - Confirm Python version:
     ```bash
     python --version  # Should show Python 3.12.x
     ```

5. **Upgrade pip and Install Build Tools**
   ```bash
   pip install --upgrade pip setuptools wheel
   ```

6. **Install Required Package**
   ```bash
   pip install faster-whisper
   ```
   - This installs `faster-whisper` and its dependencies (e.g., `av`) seamlessly on Python 3.12.

## How to Use

1. **Basic Usage**
   ```bash
   python transcribe.py <path-to-your-audio-file>
   ```

2. **Example Usage**
   ```bash
   python transcribe.py recording.mp3
   ```
   - If no file is specified, it defaults to `audio.mp3` in the current directory.

The tool will:
- Load the large-v2 Whisper model
- Detect the language automatically
- Provide timestamps for each segment
- Display the transcribed text

## Output Format

The program outputs:
- Language detection with confidence score
- Timestamped transcription segments
- Example output:
  ```
  Detected language: en with probability: 0.95
  [0.00s -> 2.50s] This is an example transcription...
  ```

## Project Structure

```
transcriber/
├── transcribe.py    # Main transcription script
├── README.md        # This documentation
└── venv/            # Virtual environment (after setup)
```

## Troubleshooting

1. **Installation Fails with `ModuleNotFoundError: No module named 'Cython'`**
   - Ensure you ran `pip install --upgrade pip setuptools wheel` before installing `faster-whisper`.

2. **Cython Compilation Errors (e.g., `noexcept` issues)**
   - This occurs with Python 3.13. Switch to Python 3.12:
     ```bash
     deactivate
     rm -rf venv
     python3.12 -m venv venv
     source venv/bin/activate
     pip install --upgrade pip setuptools wheel
     pip install faster-whisper
     ```

3. **FFmpeg Not Found**
   - Verify installation with `ffmpeg -version`. Reinstall if missing (see Step 2 above).

4. **Memory Issues**
   - The large-v2 model needs ~4-8GB RAM during inference. For low memory, edit `transcribe.py` to use a smaller model (e.g., `"medium"` instead of `"large-v2"`).

5. **Performance**
   - Transcription speed varies with CPU power (expect 1-2x real-time). Ensure supported audio formats (MP3, WAV, M4A).

## Technical Details

- **Model**: Faster Whisper large-v2
- **Compute Type**: INT8 quantization (for CPU efficiency)
- **Device**: CPU
- **Beam Size**: 5 (for improved accuracy)

## Script Code

For reference, here’s the `transcribe.py` script this README supports:

```python
from faster_whisper import WhisperModel
import sys

model_size = "large-v2"
model = WhisperModel(model_size, device="cpu", compute_type="int8")

def main():
    if len(sys.argv) > 1:
        audio_file = sys.argv[1]
    else:
        audio_file = "audio.mp3"

    segments, info = model.transcribe(audio_file, beam_size=5)

    print(f"\nDetected language: {info.language} with probability: {info.language_probability:.2f}")
    print("\nTranscription:")
    for segment in segments:
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

if __name__ == "__main__":
    main()
```

## Need Help?

If you encounter issues:
1. Check Python version (`python --version` should show 3.12.x).
2. Verify FFmpeg (`ffmpeg -version`).
3. Ensure sufficient resources (RAM, disk space).
4. Match error messages to troubleshooting steps.

Happy Transcribing! 🎉
