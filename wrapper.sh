#!/bin/bash
# script bash pour tout faire rouler ensemble

date_heure=$(date +%y%m%d_%H%M%S)
mv donnees_skidefond.json donnees_skidefond.$date_heure.json

./obtenir_toutes_conditions.py
./skidefond.py
