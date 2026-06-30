import librosa
import numpy as np

def extract_features(file):

    audio, sr = librosa.load(file, sr=None)

    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=20)

    features = np.mean(mfcc.T, axis=0)

    return features.reshape(1,-1)