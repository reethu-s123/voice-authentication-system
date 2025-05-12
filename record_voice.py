import sounddevice as sd
import soundfile as sf
import numpy as np

def record_voice(filename="reference_voice.wav", duration=5, sr=22050):
    print("Recording... Speak now!")
    audio = sd.rec(int(duration * sr), samplerate=sr, channels=1, dtype=np.float32)
    sd.wait()
    sf.write(filename, audio, sr)
    print(f"Voice recorded and saved as {filename}")

if __name__ == "__main__":
    record_voice()
