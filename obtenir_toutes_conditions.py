#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Extraire information sur les conditions de ski de fond dans les parcs de l'île de Montréal

À faire:
- Régler les soucis d'accents
'''

import yaml, json, time
import requests
from bs4 import BeautifulSoup

def charger_liste(fichier_liste_parcs):

    # charger la liste des parcs à analyser, en YAML
    with open(fichier_liste_parcs, 'r') as fichier:
        liste_parcs = yaml.load(fichier)

    return(liste_parcs)

def faire_requete(id_parc, num_activite, url_base):

    # définir payload comme tuple pour envoyer paramètres dans l'ordre défini
    payload = (('id', id_parc), ('sc', num_activite))

    # effectuer la requête et vérifier le code du status
    requete = requests.get(url_base, params = payload)

    if requete.status_code != 200:
        print('Information non disponible')

    # vérifier le id_parc et effectuer la soupe correspondante
    else:
        #Mont-Royal
        if id_parc == 81:
            nom_parc, conditions = soupe_montroyal(requete)
            #print(nom_parc)
            #print(conditions)

        #Bois-de-Liesse
        elif id_parc == 72:
            nom_parc, conditions = soupe_boisliesse(requete)
            #print(nom_parc)
            #print(conditions)

        #Île-Bizard
        elif id_parc == 73:
            nom_parc, conditions = soupe_ilebizard(requete)
            #print(nom_parc)
            #print(conditions)

        #Cap-Saint-Jacques
        elif id_parc == 74:
            nom_parc, conditions = soupe_capstjacques(requete)
            #print(nom_parc)
            #print(conditions)

        #Île-de-la-visitation
        elif id_parc == 75:
            nom_parc, conditions = soupe_visitation(requete)
            #print(nom_parc)
            #print(conditions)

        #Pointe-aux-Prairies
        elif id_parc == 82:
            nom_parc, conditions = soupe_pointeprairie(requete)
            #print(nom_parc)
            #print(conditions)

        else:
            print('Erreur')

    return(nom_parc, conditions)

def soupe_montroyal(requete):

    # faire la soupe
    page = BeautifulSoup(requete.text, 'html.parser')

    # extraire l'information pertinente
    section_info = page.find('div', {'class' : 'fiche_contenu'})
    nom_parc = section_info.find('h1').text

    section_pistes = section_info.find('div', {'class' : 'a_noter'})
    pistes = section_pistes.find_all('p')

    section_etat = section_info.find_all('h3')

    conditions = {'État des pistes de ski' : section_etat[0].text,
                  'Qualité de la neige' : section_etat[9].text,
                  'Enneigement' : section_etat[10].text,
                  'Commentaires' : pistes[3].text
                  }

    return(nom_parc, conditions)

def soupe_boisliesse(requete):

    # faire la soupe
    page = BeautifulSoup(requete.text, 'html.parser')

    # extraire l'information pertinente
    section_info = page.find('div', {'class' : 'fiche_contenu'})
    nom_parc = section_info.find('h1').text

    section_pistes = section_info.find('div', {'class' : 'a_noter'})
    pistes = section_pistes.find_all('p')

    section_etat = section_info.find_all('h3')

    conditions = {'État des pistes de ski' : section_etat[0].text,
                  'Qualité de la neige' : section_etat[4].text,
                  'Enneigement' : section_etat[5].text,
                  'Commentaires' : pistes[3].text
                  }

    return(nom_parc, conditions)

def soupe_ilebizard(requete):

    # faire la soupe
    page = BeautifulSoup(requete.text, 'html.parser')

    # extraire l'information pertinente
    section_info = page.find('div', {'class' : 'fiche_contenu'})
    nom_parc = section_info.find('h1').text

    section_pistes = section_info.find('div', {'class' : 'a_noter'})
    pistes = section_pistes.find_all('p')

    section_etat = section_info.find_all('h3')

    conditions = {'État des pistes de ski' : section_etat[0].text,
                  'Qualité de la neige' : section_etat[3].text,
                  'Enneigement' : section_etat[4].text,
                  'Commentaires' : pistes[3].text
                  }

    return(nom_parc, conditions)

def soupe_capstjacques(requete):

    # faire la soupe
    page = BeautifulSoup(requete.text, 'html.parser')

    # extraire l'information pertinente
    section_info = page.find('div', {'class' : 'fiche_contenu'})
    nom_parc = section_info.find('h1').text

    section_pistes = section_info.find('div', {'class' : 'a_noter'})
    pistes = section_pistes.find_all('p')

    section_etat = section_info.find_all('h3')

    conditions = {'État des pistes de ski' : section_etat[0].text,
                  'Qualité de la neige' : section_etat[4].text,
                  'Enneigement' : section_etat[5].text,
                  'Commentaires' : pistes[4].text
                  }

    return(nom_parc, conditions)

def soupe_visitation(requete):

    # faire la soupe
    page = BeautifulSoup(requete.text, 'html.parser')

    # extraire l'information pertinente
    section_info = page.find('div', {'class' : 'fiche_contenu'})
    nom_parc = section_info.find('h1').text

    section_pistes = section_info.find('div', {'class' : 'a_noter'})
    pistes = section_pistes.find_all('p')

    section_etat = section_info.find_all('h3')

    conditions = {'État des pistes de ski' : section_etat[0].text,
                  'Qualité de la neige' : section_etat[3].text,
                  'Enneigement' : section_etat[4].text,
                  'Commentaires' : pistes[3].text
                  }

    return(nom_parc, conditions)

def soupe_pointeprairie(requete):

    # faire la soupe
    page = BeautifulSoup(requete.text, 'html.parser')

    # extraire l'information pertinente
    section_info = page.find('div', {'class' : 'fiche_contenu'})
    nom_parc = section_info.find('h1').text

    section_pistes = section_info.find('div', {'class' : 'a_noter'})
    pistes = section_pistes.find_all('p')

    section_etat = section_info.find_all('h3')

    conditions = {'État des pistes de ski' : section_etat[0].text,
                  'Qualité de la neige' : section_etat[4].text,
                  'Enneigement' : section_etat[5].text,
                  'Commentaires' : pistes[3].text
                  }

    return(nom_parc, conditions)

def enregistrer_donnees(nom_parc, conditions, resultats):

    # créer le dictionnaire resultat et y mettre les conditons de ski pour le parc
    resultats['parc'].append({nom_parc : conditions})

    return(resultats)

def creer_fichier_sortie(resultats):

    # créer un objet en format json
    donnees = json.dumps(resultats)

    # sauvegarder fichier json
    with open('donnees_skidefond.json', 'w', encoding='utf8') as fichier_sortie:
        json.dump(donnees, fichier_sortie)

def main():

    url_base = 'http://ville.montreal.qc.ca/portal/page?_pageid=7377,94551572&_dad=portal&_schema=PORTAL'
    fichier_liste_parcs = 'liste_parcs.yml'
    liste_id_parcs = []
    resultats = {}
    resultats['parc'] = []

    # numéro de l'activité pour le ski de fond sur le site de la Ville de Montréal
    num_activite = 7

    # charger information sur les parcs
    liste_parcs = charger_liste(fichier_liste_parcs)

    # créer liste des numéros ('id') des parcs
    for parc in range(len(liste_parcs)):
        for details in liste_parcs[parc]:
            liste_id_parcs.append(liste_parcs[parc][details]['id'])

    # pour chaque parc, extraire les données sur les conditions de ski
    for id_parc in liste_id_parcs:
        nom_parc, conditions = faire_requete(id_parc, num_activite, url_base)
        resultats = enregistrer_donnees(nom_parc, conditions, resultats)

    creer_fichier_sortie(resultats)


if __name__ == '__main__':
    main()
