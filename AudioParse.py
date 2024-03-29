import os
import re
import librosa
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout


class AudioParse:

    def __init__(self, audio_file_root):
        self.audio_file_root = audio_file_root
        self.audio_file_emotion = []
        self.audio_file_feature = []
        self.audio_file_label = []

    def getlabels(self):
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.audio_file_root):
            for file in f:
                if '.wav' in file:
                    files.append(file)

        for file_name in files:
            file_name_split = re.split('[_.]', file_name)
            self.audio_file_emotion.append((file_name, file_name_split[2]))
        # print(sound_file_label)

    def derive_features(self):
        for file_name, emotion in self.audio_file_emotion:
            audio_file_full_path = self.audio_file_root + file_name
            print("Extracting feature for " + audio_file_full_path)
            try:
                # here kaiser_fast is a technique used for faster extraction
                X, sample_rate = librosa.load(audio_file_full_path, res_type='kaiser_fast')
                # we extract mfcc feature from data
                mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            except IOError as e:
                print("Error encountered while parsing file: ", file_name)

            self.audio_file_feature.append(mfccs)
            self.audio_file_label.append(emotion)
        # print(self.audio_file_label)

    def label_encoding(self):
        np_label = np.array(self.audio_file_label)
        np_features = np.array(self.audio_file_feature)

        lb = LabelEncoder()
        # np_label = np_utils.to_categorical(lb.fit_transform(np_label))
        np_label_encoded = lb.fit_transform(np_label)
        y = np_utils.to_categorical(np_label_encoded)
        print(list(np_label_encoded))

        num_labels = y.shape[1]
        filter_size = 2

        # build model
        model = Sequential()

        model.add(Dense(256, input_shape=(40,)))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))

        model.add(Dense(256))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))

        model.add(Dense(num_labels))
        model.add(Activation('softmax'))

        model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
        model.fit(np_features, y, batch_size=32, epochs=5, validation_split=0.1)
