import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os


def getlabels(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.wav' in file:
                files.append(file)
    return files


path = '/home/dgrfi/Documents/WavData/All/'

print(path)

#
# getLabels(path)
# for f in files:
#    print(f)
# data, sampling_rate = librosa.load('/home/dgrfi/Documents/WavData/All/OAF_back_angry.wav')
# plt.figure(figsize=(12, 4))
# librosa.display.waveplot(data, sr=22050)
# mfccs = librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40)
# print(mfccs.shape)
