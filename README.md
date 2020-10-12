# Detection d'un genre d'une musique

Le but de l'algoritme est de prédire le genre de la musique en fonction de 10 possibilités : 
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

Pour cela nous avons établi un modèle via Keras à partir d'un échantillon de données pour 1000 fichiers audios (100 musiques par genre) qui se trouve dans le fichier data.csv  

La prédiction se fait à partir d'un lien youtube.  

### Les étapes

1. Téléchargement de la musique youtube en fichier .mp3  
2. Conversion de la musique de .mp3 en .wav  
3. Crétion d'un csv pour contenir les caractéristiques de la musique  
4. Remplissage du csv avec les caractéristiques de la musique
5. Faire passer ces données dans notre modèle afin de détecter le genre de la musique

### Faire fonctionner l'algorithme  

**Attention** : les chemin absolu dans les algorithmes sont en local, ils font donc les modifier pour faire marcher l'algorithme  

Aller dans le dossier python_script et lancer la commande   
```
streamlit run streamlite.py
```

