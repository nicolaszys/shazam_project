# Streamlit
import streamlit as st

# Import de mes fonction
from youtube import youtube_to_mp3
###
from audio import audio_conversion
from audio import audio_csv
from audio import empty_csv
###
from shazam import shazam
#from shazam import model_result

# time 
import time

# csv 
import csv 


# Ttitle
st.title("Find your music type")

# Subtitle
st.subheader("Upload your music")

#def music_choice():
link = st.text_input('Enter a youtube url:')
try:
    st.video(link)
except FileNotFoundError:
    st.error('File not found.')

# convert youtube link to mp3 audio
audio = youtube_to_mp3(link)
print(f"youtube is : {audio}")
print("audio telecharge")

# time wait
time.sleep(1)

# convert mp3 audio to wav audio
audio_conversion(audio)
print(f"wav is: {audio}")
print('audio convertie')

# create an empty csv file
empty_csv(audio)
print(f"empty_csv is: {audio}")


# convert audio.wav to data and append in csv file created precedently
audio_csv(audio)
print(f"data is : {audio}")


# model
shazam(audio)
print("model done")
print(f"model is : {audio}")






