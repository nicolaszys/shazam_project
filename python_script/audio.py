# Librosa
import librosa
import librosa.display
import IPython.display as ipd

# Classics
import os
from PIL import Image
import pathlib
import csv
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd

# Autres
import warnings
warnings.filterwarnings('ignore')

# Audio segment
from pydub import AudioSegment

# Import de mes fonctions 
from youtube import youtube_to_mp3

# Import csv
import csv

## --> give an audio path
## --> audio path is given by an upload via streamlit
def audio_conversion(audio):
    # audio upload & audio convertion in a wav file
    # audio_path_mp3 = f"../songs/mp3/{audio}.mp3"
    # dst = f"../songs/converted/{audio}.wav"
    audio_path_mp3 = f"../songs/mp3/{audio}.mp3"
    dst = f"../songs/converted/{audio}.wav"
    sound = AudioSegment.from_file(audio_path_mp3)
    sound.export(dst, format="wav")
    audio_path_wav = f'../songs/converted/{audio}.wav'
    x , sr = librosa.load(audio_path_wav)
    return audio

def empty_csv(audio):
    # create audio file caracteristics
    header = 'filename chroma_stft spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
    for i in range(1, 21):
        header += f' mfcc{i}'
    header += ' label'
    header = header.split()
    with open(f'/Users/macbook/Desktop/shazam_project_git/result/{audio}.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
    return audio

def audio_csv(audio):
    songname = f'/Users/macbook/Desktop/shazam_project_git/songs/converted/{audio}.wav'
    y, sr = librosa.load(songname, mono=True, duration=30)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    to_append = f'{audio} {np.mean(chroma_stft)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'    
    for e in mfcc:
        to_append += f' {np.mean(e)}'
    #to_append += f' {g}'
    file = open(f'/Users/macbook/Desktop/shazam_project_git/result/{audio}.csv', 'a', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(to_append.split())
    return audio

 #### Function below has been integrated to shazam() function   

# def csv_prep(audio):
#     df = pd.read_csv(f'/Users/macbook/Desktop/shazam_project/result/{audio}.csv')
#     df.drop(['filename','label'], axis=1, inplace=True)
#     scaler = StandardScaler()
#     scaler.fit_transform(np.array(df.iloc[:,:], dtype = float))
#     return audio, df
