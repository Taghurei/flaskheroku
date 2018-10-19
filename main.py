#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request
from flask_cors import CORS
import unidecode
app = Flask(__name__)
CORS(app)
import Stop_words

@app.route('/')
@app.route('/coucou/')
def index():
   return "hello to the flask app"

@app.route('/envoi', methods=['POST'])
def envoi():
    inputted_json = request.get_json(force=True) #On recupère le JSON envoyé par le parser linkedIn
    Liste_tag_garde=[] # On définit la liste des tags qu'on gardera
    tag=["Java","C++","CentraleSupélec","Master","Paris","Nantes","centraledigitallab","Gauthier Lacroix","engineer","internship","student","technology","Developer","Agile","Scrum","Prototyper"]    
    for k in range (len(tag)):
        tag[k] = unidecode.unidecode(tag[k].lower()) #On enlève les caractères speciaux et les majuscules de notre liste de tag
    liste_mot_utile=[]
    stop_words = Stop_words.stopwords #definiton des mots a retirer
    for key,value in (inputted_json.items()):#parcours du dictionnaire
        if (type(value) is dict):#et du dictionnaires de dictionnaires (boucle double for obligatoire)
            for key,value in value.items():
                if (value):
                    word_tokens = (unidecode.unidecode(value.lower())).split()#recuperation des donnees du dictionnaire ainsi que la position de la cle
                    filtered_sentence = [w for w in word_tokens if not w in stop_words] #parcourt des mots des strings
                    for w in word_tokens: 
                        if w not in stop_words: #recuperation des mots utiles
                            filtered_sentence.append(w) 
                    liste_mot_utile.append(list(set(filtered_sentence)))
    for i in (liste_mot_utile): #on parcourt la liste de mot et la liste de tag
        for j in (i):
            for k in tag:
                if (j==k): # En cas d'égalité on ajoute le tag dans la liste des tag ressortis
                    Liste_tag_garde.append(k)
    return 'Tag ressorti: %s' % list(set(Liste_tag_garde)) # On renvoie dans la console les tags ressortis

if __name__ == '__main__':
    app.run()
