# Streamlit
import streamlit as st

# Librosa
import librosa
import librosa.display
import IPython.display as ipd

# Classics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
import pathlib
import csv

# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Autres
import warnings
warnings.filterwarnings('ignore')

#Keras
import keras
from keras import models
from keras import layers

###### Extracting features from spectrogram

header = 'filename chroma_stft spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
for i in range(1, 21):
    header += f' mfcc{i}'
header += ' label'
header = header.split()

## Analysing the Data in Pandas
def shazam(audio):
    ####
    # MODEL
    ####

    data = pd.read_csv(f"/Users/macbook/Desktop/shazam_project_git/data.csv")

    # Dropping unneccesary columns
    data = data.drop(['filename'],axis=1)

    ### Encoding labels
    encoder = LabelEncoder()
    y = encoder.fit_transform(data.iloc[:, -1])

    ### Scaling feature columns
    scaler = StandardScaler()
    X = scaler.fit_transform(np.array(data.iloc[:, :-1], dtype = float))

    ### Dividing data into training and testing set 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    ### Classification with Keras
    model = models.Sequential()
    model.add(layers.Dense(256, activation='relu', input_shape=(X_train.shape[1],)))

    model.add(layers.Dense(128, activation='relu'))

    model.add(layers.Dense(64, activation='relu'))

    model.add(layers.Dense(10, activation='softmax'))

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=100, batch_size=128)

    ### Validating our approach
    x_val = X_train[:200]
    partial_x_train = X_train[200:]

    y_val = y_train[:200]
    partial_y_train = y_train[200:]

    model = models.Sequential()
    model.add(layers.Dense(512, activation='relu', input_shape=(X_train.shape[1],)))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    model.fit(partial_x_train,
            partial_y_train,
            epochs=100,
            batch_size=512,
            validation_data=(x_val, y_val))

    model.evaluate(X_test, y_test)
    
    #####
    # PREDICTION
    #####
    df = pd.read_csv(f'/Users/macbook/Desktop/shazam_project_git/result/{audio}.csv')
    df = df.drop(['filename','label'], axis=1)
    scaler = StandardScaler()
    scaler.fit_transform(np.array(df.iloc[:,:], dtype = float))
    music_type = model.predict(df)
    music_style = {0: "blues", 1: "classical", 2:'country', 3:'disco', 4:'hiphop', 5:'jazz', 6:'metal', 7:'pop', 8:'reggae', 9:'rock'}
    result = music_style[music_type.argmax()]

    print(result)
    st.title(f"Your music is a : {result} music")


#### Function below has been integrated to shazam() function   

# def model_result(audio, model):
#     music_type = model.predict(f"/Users/macbook/Desktop/shazam_project/result/{audio}.csv")
#     music_style = {0: "blues", 1: "classical", 2:'country', 3:'disco', 4:'hiphop', 5:'jazz', 6:'metal', 7:'pop', 8:'reggae', 9:'rock'}
#     result = music_style[music_type.argmax()]
#     return result