#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Extraire information sur les conditions de ski de fond dans un parc spécifique de l'île de Montréal

À faire:
- Régler les soucis d'accents
'''

import json
#from sopel.module import commands, example

def trouver_conditions(nom_fichier, nom_parc):

    with open(nom_fichier, 'r') as fichier:
        donnees_json = json.loads(fichier.read())


    print(type(donnees_json))
    print(donnees_json["parc"]["Parc du Mont-Royal"])

    conditions = []
    return(conditions)


#@commands('skidefond')
#@example('.skidefond Mont-Royal')
#def main(bot, trigger):
def main():

    #url_fichier = 'https://www.normandcyr.com/data/donnees_skidefond.json'
    nom_fichier = 'donnees_skidefond2.json'

    nom_parc = 'Mont-Royal'

    conditions = trouver_conditions(nom_fichier, nom_parc)
    print(conditions)

if __name__ == '__main__':
    main()
