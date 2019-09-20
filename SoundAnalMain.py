from AudioParse import AudioParse

audio_file_path = '/home/dgrfi/Documents/WavData/All/'
audio_parse = AudioParse(audio_file_path)
audio_parse.getlabels()
audio_parse.derive_features()
audio_parse.label_encoding()
print("Done")
#
# getLabels(path)
# for f in files:
#    print(f)
# data, sampling_rate = librosa.load('/home/dgrfi/Documents/WavData/All/OAF_back_angry.wav')
# plt.figure(figsize=(12, 4))
# librosa.display.waveplot(data, sr=22050)
# mfccs = librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40)
# print(mfccs.shape)