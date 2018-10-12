#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_cors import CORS
import unidecode
app = Flask(__name__)


@app.route('/')
@app.route('/coucou/')
def index():
   return "hello to the flask app"

@app.route('/envoi', methods=['POST'])
def envoi():
    tag='[Java,C++,CentraleSupélec,Master,Paris,Nantes,centraledigitallab,Gauthier Lacroix,engineer,internship,student,technology,Developer,Agile,Scrum,Prototyper]'#On definit la liste de tag dans la fonction (A AMELIORER)
    inputted_json = request.get_json(force=True) #On recupère le JSON envoyé par le parser linkedIn
    tag = unidecode.unidecode(tag.lower()) #On enlève les caractères speciaux et les majuscules de notre liste de tag
    liste_mot=[] #on definit la liste de mots contenus dans le JSON
    Liste_tag_garde=[] # On définit la liste des tags qu'on gardera
    tag=tag.split(',')#on formatte les tags comme voulu (peut devenir inutile selon notre nouvelle definiton de tags)
    for i in inputted_json.keys(): #on parcourt le dictionnaire pour recuperer les différents élements (chaque clé doit etre conserver pour la suite)
        if (type(inputted_json[i]) is dict): #si le dictionnaire contient des dictionnaires on les distingue aussi
            for j in inputted_json[i].keys(): 
                l=(unidecode.unidecode(inputted_json[i][j].lower()))#On enlève les caractères speciaux et les majuscules de notre liste
                for k in (l.split(' ')): #On separe chaque groupe de mots obtenus pour n'avoir que des mots simples
                    for z in k.split(','):
                        liste_mot.append(z) #on ajoute les mots obtenus a notre liste de mots
        if (type(inputted_json[i]) is str): # On réalise les mêmes étapes pour les autres parties du dictionnaires
            l=(unidecode.unidecode(inputted_json[i].lower()))
            for k in (l.split(' ')):
                for z in k.split(','):
                    liste_mot.append(z)
    liste_mot = list(set(liste_mot)) #On enlève les mots en double dans la liste
    for i in liste_mot: #on parcourt la liste de mot et la liste de tag
            for k in tag:
                if (i==k): # En cas d'égalité on ajoute le tag dans la liste des tag ressortis
                    Liste_tag_garde.append(k)
    return 'Tag ressort i:  %s' % list(set(Liste_tag_garde)) # On renvoie dans la console les tags ressortis

if __name__ == '__main__':
    app.run()
