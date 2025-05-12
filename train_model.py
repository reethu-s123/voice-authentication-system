import librosa
import numpy as np
import pickle


def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=22050)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfccs.T, axis=0)


def train_model():
    feature = extract_features("reference_voice.wav")
    model = {"reference_voice": feature}

    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model trained and saved.")


if __name__ == "__main__":
    train_model()
