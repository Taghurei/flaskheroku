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
    word_tokens=[]
    tag=["Java","C++","CentraleSupélec","Master","Paris","Nantes","centraledigitallab","Gauthier Lacroix","engineer","internship","student","technology","Developer","Agile","Scrum","Prototyper"]    
    for k in range (len(tag)):
        tag[k] = unidecode.unidecode(tag[k].lower()) #On enlève les caractères speciaux et les majuscules de notre liste de tag
    liste_mot_utile=[]
    stop_words = Stop_words.stopwords #definiton des mots a retirer
    for key,value in (inputted_json.items()):#parcours du dictionnaire
        if (type(value) is dict):#et du dictionnaires de dictionnaires (boucle double for obligatoire)
            for key,value in value.items():
                if (value):
                 for k in ((unidecode.unidecode(value)).split(' ')): #On separe chaque groupe de mots obtenus pour n'avoir que des mots simples
                    for z in k.split(','):
                        word_tokens.append(z.lower()) #on ajoute les mots obtenus a notre liste de mots
                filtered_sentence = [w for w in word_tokens if not w in stop_words] #parcourt des mots des strings
    print(filtered_sentence)
    print(tag)
    for i in (filtered_sentence): #on parcourt la liste de mot et la liste de tag
        for k in tag:
            if (i==k): # En cas d'égalité on ajoute le tag dans la liste des tag ressortis
                print("er")
                Liste_tag_garde.append(k)
    return 'Tag ressorti: %s' % list(set(Liste_tag_garde)) # On renvoie dans la console les tags ressortis

if __name__ == '__main__':
    app.run()
