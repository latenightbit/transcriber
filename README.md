# Audio Transcriber

A Python tool that converts audio files into text using the Faster Whisper model (large-v2). This implementation uses CPU-based inference optimized for general use.

## What Does This Tool Do?

This tool transcribes audio files into text using the Faster Whisper model, which is an efficient implementation of OpenAI's Whisper model.

## Key Features

- 🎵 Works with common audio formats (MP3, WAV, M4A)
- 🎯 Uses the large-v2 model for high accuracy
- 🌍 Supports multiple languages with automatic language detection
- 💻 Simple command line interface
- 🚀 Optimized for CPU usage with INT8 quantization

## System Requirements

1. **Python**: Python 3.x
   - Check version: `python --version`
   - Download from [Python's official website](https://www.python.org/downloads/)

2. **Hardware**:
   - Sufficient RAM (recommended: 8GB+)
   - Adequate disk space for the model
   - CPU with good single-thread performance

## Installation Guide

1. **Download the Project**
   ```bash
   git clone <repository-url>
   cd transcriber
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Required Package**
   ```bash
   pip install faster-whisper
   ```

## How to Use

1. **Basic Usage**
   ```bash
   python transcribe.py <path-to-your-audio-file>
   ```

2. **Example Usage**
   ```bash
   python transcribe.py recording.mp3
   ```

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
├── transcribe.py     # Main transcription script
└── README.md        # Documentation
```

## Troubleshooting

1. **Memory Issues**
   - The large-v2 model requires significant RAM
   - Consider using a smaller model size if experiencing memory problems

2. **Performance**
   - The tool uses CPU with INT8 quantization for balanced performance
   - Transcription speed depends on your CPU capabilities

## Technical Details

- Model: Faster Whisper large-v2
- Compute Type: INT8 quantization
- Device: CPU
- Beam Size: 5 (for improved accuracy)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Need Help?

If you encounter issues:
1. Check your Python version and dependencies
2. Verify audio file format compatibility
3. Ensure sufficient system resources
4. Check the error messages for specific issues

Happy Transcribing! 🎉