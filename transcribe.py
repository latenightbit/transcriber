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

