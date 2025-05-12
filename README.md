# voice-authentication-system
This project implements a Voice Authentication System using Python, Librosa, and Machine Learning (SVM/GMM). It's a Master in Computer Applications (Cyber Security) project for GM University.

## Project Overview
The system captures a user's voice, extracts Mel-Frequency Cepstral Coefficients (MFCCs), trains a model, and then authenticates users by comparing new voice samples to the stored voiceprint.

## Features
- Voice recording
- MFCC feature extraction
- Model training (e.g., SVM)
- Voice verification

## Technologies Used
- Python 3.x
- Librosa
- Scikit-learn
- NumPy
- PyAudio (or sounddevice/soundfile)
- Joblib (or pickle)

## How to Run
1.  *Prerequisites:*
    *   Install Python 3.7+
    *   Clone this repository: git clone https://github.com/reethu-s123/voice-authentication-system.git
    *   Navigate to the project directory: cd voice-authentication-system
    *   Install required libraries: pip install -r requirements.txt
2.  *Enrollment (Training):*
    *   Run python record_voice.py to record your reference voice (e.g., reference_voice.wav).
    *   Run python train_model.py to train the model using the reference voice and save model.pkl.
3.  *Authentication:*
    *   Run python verify_voice.py. This will prompt you to speak, record a new voice sample (e.g., test_voice.wav), and then compare it against the trained model.

## Authors
- Reethu S (P24C01CA055)

## Project Report
The detailed project report can be found [here](VoiceAuthSystem.pdf).
