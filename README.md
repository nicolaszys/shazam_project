# Detection d'un genre d'une musique

Le but de l'algoritme est de prédire le genre de la musique en fonction de 10 genres : 
 - blues
 - classique
 - country
 - disco
 - hiphop
 - jazz
 - metal
 - pop
 - reggae
 - rock  

Pour cela nous avons établi un modèle via Keras à partir d'un échantillon de données pour 1000 fichiers audios (100 musiques par genre) qui se trouve dans le fichier data.csvv  

Ce fichier donne les caractéristiques pour la musique comme le :  
- Zero Crossing Rate : the rate of sign-changes along a signal, i.e., the rate at which the signal changes from positive to negative or back.  
- Spectral Centroid : It indicates where the ”centre of mass” for a sound is located and is calculated as the weighted mean of the frequencies present in the sound.  
- Spectral Rolloff : It is a measure of the shape of the signal. It represents the frequency below which a specified percentage of the total spectral energy.  
- Mel-Frequency Cepstral Coefficients : The Mel frequency cepstral coefficients (MFCCs) of a signal are a small set of features (usually about 10–20) which concisely describe the overall shape of a spectral envelope. It models the characteristics of the human voice.  
- Chroma Frequencies : Chroma features are an interesting and powerful representation for music audio in which the entire spectrum is projected onto 12 bins representing the 12 distinct semitones (or chroma) of the musical octave.  


La prédiction se fait à partir d'un lien youtube.  

### Les étapes

1. Téléchargement de la musique youtube en fichier .mp3  
2. Conversion de la musique de .mp3 en .wav  
3. Crétion d'un csv pour contenir les caractéristiques de la musique  
4. Remplissage du csv avec les caractéristiques de la musique
5. Faire passer ces données dans notre modèle afin de détecter le genre de la musique

### Faire fonctionner l'algorithme  

**Attention** : les chemins absolus dans les algorithmes sont en local, ils font donc les modifier pour faire marcher l'algorithme. 

Aller dans le dossier python_script et lancer la commande :  
```
streamlit run streamlite.py
```

