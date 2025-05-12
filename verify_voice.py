import pickle
import numpy as np
from record_voice import record_voice
from train_model import extract_features


def verify_voice():

    record_voice(filename="test_voice.wav")


    new_feature = extract_features("test_voice.wav")


    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
        print("✅ Model loaded successfully!")


    reference_feature = model.get("reference_voice")


    if reference_feature is None or new_feature is None:
        print("❌ Error: Could not extract valid features for comparison.")
        return


    if reference_feature.shape != new_feature.shape:
        print(f"❌ Shape mismatch: reference_feature={reference_feature.shape}, new_feature={new_feature.shape}")
        return


    similarity = np.linalg.norm(reference_feature - new_feature)


    threshold = 40
    if similarity < threshold:
        print("✅ Voice Matched!")
    else:
        print("❌ Voice Not Recognized!")



if __name__ == "__main__":
    verify_voice()