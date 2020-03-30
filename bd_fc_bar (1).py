# -*- coding: utf-8 -*-

#  Envoi des données dans une BD (phpMyAdmin)
#   Mettre ce fichier et 'fiche_equipe.py' dans le même dossier

import fiche_equipe
import stats_joueurs
import r_matchs
import pymysql as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "bd_football"
)

cursor = db.cursor()

# Appel des fonctions du fichier 'fiche_equipe'

#n_equipe = fiche_equipe.club_info()
#jrs = fiche_equipe.joueurs()
#d_match = fiche_equipe.DernMatch()
#stats_j = fiche_equipe.statJoueur()
#nom_j = stats_joueurs.nom_joueur()
#club_act = stats_joueurs.club_actuel()
#tpa = stats_joueurs.taille_poids_age()
#performance = stats_joueurs.perfo()
matchs_o = r_matchs.resMatch()
score_o = r_matchs.score()
statut_o = r_matchs.statut()
horaire_o = r_matchs.horaire()


### INSERTION JOUEURS

#for x in jrs:
#    req = "INSERT INTO joueurs_liga(nom_equipe, joueurs, dernier_match) VALUES ('{}', '{}', '{}')".format(n_equipe, x, d_match)
#    cursor.execute(req)
#    db.commit()

### INSERTION STATS
#for x, y, z, e in zip(nom_j, club_act, tpa, performance):
#    req = "INSERT INTO stats_joueurs3(nom_joueur, club_actuel, taille_poids_age, niveau_general) VALUES ('{}', '{}', '{}', '{}')".format(x, y, z, e)
#    cursor.execute(req)

for f, s, u, p in zip(matchs_o, score_o, statut_o, horaire_o):
    req = "INSERT INTO matchs_es(matchs, score, statut, horaire) VALUES ('{}', '{}', '{}', '{}')".format(f, s, u, p)
    cursor.execute(req)

    db.commit()
        

db.close()



