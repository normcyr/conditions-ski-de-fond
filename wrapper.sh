#!/bin/bash
# script bash pour tout faire rouler ensemble

# renommer ancien fichier
#date_heure=$(date +%y%m%d_%H%M%S)
#mv /var/www/html/normandcyr.com/apps/data/skidefond/donnees_skidefond.json /var/www/html/normandcyr.com/apps/data/skidefond/donnees_skidefond.$date_heure.json

# aller chercher les conditions actuelles
/home/norm/Softwares/git/conditions-ski-de-fond/obtenir_toutes_conditions.py

# copier dans dossier accessible sur le web
chmod 644 "/home/norm/Softwares/git/conditions-ski-de-fond/donnees_skidefond.json"
#mv "/home/norm/git/conditions_ski_de_fond/donnees_skidefond.json" "/var/www/html/normandcyr.com/apps/data/skidefond/"

#./skidefond.py
