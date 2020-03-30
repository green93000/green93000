from bs4 import BeautifulSoup
import urllib.request
import csv
import re

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

#opener = AppURLopener()
#response = opener.open('https://www.footballdatabase.eu/fr/club/equipe/45-fc_barcelone')
#html_p = response.read()
#soup = BeautifulSoup(html_p, "html.parser")
##
##
#with open('output8.csv', 'w', encoding="utf-8") as csvfile:
#    csvwriter = csv.writer(csvfile)
#    lis = []
#    cc = soup.findAll("div", {"class":"player"})
#    for i in cc:
#        res = i.findAll('a', href=True)
#        for a in res:
#            fu =  a['href']
#            lis.append(fu)
#            result = list(dict.fromkeys(lis))
#            regex = re.compile(r'/fr/pays/general/\d+\-')
#            filtered = [i for i in result if not regex.match(i)]
#            regex2 = re.compile(r'[^/]')
#            filtered2 = [x for x in filtered if not regex2.match(x)]
#    for b in filtered2:
#        csvwriter.writerow([b[1:]])
            
def saison():    
    with open('output8.csv', 'r') as f:
            liste_saison = []
            spamreader = csv.reader(f)
            for i in spamreader:
                my_url = 'https://www.footballdatabase.eu/{}'.format("".join(i))
                opener = AppURLopener()
                response = opener.open(my_url)
                html_p = response.read()
                soup = BeautifulSoup(html_p, "html.parser")
                contenu_saison = soup.findAll("span", {"class":"season"})
                for c in contenu_saison:
                    saison = c.text
                    regex_saison = re.findall(r'[0-9]+/[0-9]+', saison)
                    for v in regex_saison:
                        liste_saison.append(v)
            return "\n".join(liste_saison)
##
#print(saison())


def taille_poids_age():    
    with open('output8.csv', 'r') as f:
            liste_stats = []
            spamreader = csv.reader(f)
            for i in spamreader:
                my_url = 'https://www.footballdatabase.eu/{}'.format("".join(i))
                opener = AppURLopener()
                response = opener.open(my_url)
                html_p = response.read()
                soup = BeautifulSoup(html_p, "lxml")
                inftech_joueur_tpa = soup.findAll("div", {"class":"techpage"})
                for x in inftech_joueur_tpa:
                    contenu_tpa = x.findAll("div", {"class":"player_technical"})
                    nom_joueur = contenu_tpa[0].h1.span.text
                    contenu_selec = x.findAll("div", {"class":"data secondary"})
                    contenu_taille_val = contenu_selec[0].text
                    taille = contenu_taille_val[6:-12]
                    poids = contenu_taille_val[17:]
                    contenu_age = x.findAll("span", {"class":"age"})
                    age = contenu_age[0].text
                    liste_stats.append(age)
            return liste_stats
                    
#print(taille_poids_age())
            
def nom_joueur():    
    with open('output8.csv', 'r') as f:
            liste_stats = []
            spamreader = csv.reader(f)
            for i in spamreader:
                my_url = 'https://www.footballdatabase.eu/{}'.format("".join(i))
                opener = AppURLopener()
                response = opener.open(my_url)
                html_p = response.read()
                soup = BeautifulSoup(html_p, "lxml")
                inftech_joueur_tpa = soup.findAll("div", {"class":"techpage"})
                for x in inftech_joueur_tpa:
                    contenu_tpa = x.findAll("div", {"class":"player_technical"})
                    nom_joueur = contenu_tpa[0].h1.span.text
#                    contenu_selec = x.findAll("div", {"class":"data secondary"})
#                    contenu_taille_val = contenu_selec[0].text
#                    taille = contenu_taille_val[6:-12]
#                    poids = contenu_taille_val[17:]
#                    contenu_age = x.findAll("span", {"class":"age"})
#                    age = contenu_age[0].text
                    liste_stats.append(nom_joueur)
            return liste_stats
#print(nom_joueur())        
        
def perfo():
    with open('output8.csv', 'r') as f:
            perf = []
            spamreader = csv.reader(f)
            for i in spamreader:
                my_url = 'https://www.footballdatabase.eu/{}'.format("".join(i))
                opener = AppURLopener()
                response = opener.open(my_url)
                html_p = response.read()
                soup = BeautifulSoup(html_p, "lxml")
                inftech_joueur_perfo = soup.findAll("div", {"class":"techpage"})
                for x in inftech_joueur_perfo:
                    contenu_perfo = x.findAll("div", {"class":"player_technical"})
                    for n in contenu_perfo: 
                        physique_c = n.findAll("span", attrs= {"property":"ratingValue"})
                        for l in physique_c:
                            perf.append(l.text)
#                physique = perf[0] + "\n" + "Mental:" + "\t" + "\t" + perf[1] + "\n" + "Technique:" + "\t" + perf[2] + "\n" + "Niveau Général:" + "\t" + perf[3]
            
            return perf
    
                    
#print(perfo())
#    
            
def cartes():
    with open('output8.csv', 'r') as f:
            liste_jaune = []
            liste_rouge = []
            spamreader = csv.reader(f)
            for i in spamreader:
                my_url = 'https://www.footballdatabase.eu/{}'.format("".join(i))
                opener = AppURLopener()
                response = opener.open(my_url)
                html_p = response.read()
                soup = BeautifulSoup(html_p, "lxml")
                inftech_joueur_carte = soup.findAll("span", {"class":"league"})
                for x in inftech_joueur_carte:
                    contenu_jaune = x.findAll("span", {"class":"pc_yc2"})
                    for j in contenu_jaune:
                        carte_jaune = j.text
                        liste_jaune.append(carte_jaune)
                        
                    contenu_rouge = x.findAll("span", {"class":"pc_rc2"})
                    for r in contenu_rouge:
                        carte_rouge = r.text
                        liste_rouge.append(carte_rouge)
            return "\n" + "Cartes jaunes:" + " ".join(liste_jaune[1:]) + "\n" + "Cartes_rouges:" + " ".join(liste_rouge[1:])
#                        
                       
#print(cartes())
            
        
def buts():
    with open('output8.csv', 'r') as f:
            liste_buts = []
            spamreader = csv.reader(f)
            for i in spamreader:
                my_url = 'https://www.footballdatabase.eu/{}'.format("".join(i))
                opener = AppURLopener()
                response = opener.open(my_url)
                html_p = response.read()
                soup = BeautifulSoup(html_p, "lxml")
                inftech_joueur_buts = soup.findAll("span", {"class":"league"})
                for x in inftech_joueur_buts:
                    contenu_buts = x.findAll("span", {"class":"pc_goals2"})
                    for j in contenu_buts:
                        buts_champ = j.text
                        liste_buts.append(buts_champ)
                    
                        

            return "Buts Championnat:" + "\n" + "\n".join(liste_buts[1:])
#                        
#print(buts())
            
def club_actuel():
    with open('output8.csv', 'r') as f:
            liste_club = []
            spamreader = csv.reader(f)
            for i in spamreader:
                my_url = 'https://www.footballdatabase.eu/{}'.format("".join(i))
                opener = AppURLopener()
                response = opener.open(my_url)
                html_p = response.read()
                soup = BeautifulSoup(html_p, "lxml")
                
                inftech_club = soup.findAll("div", {"class":"player_technical"})
                for x in inftech_club:
                    contenu_club = x.findAll("h2")
                    club = contenu_club[0].text
                    liste_club.append(club)
            return liste_club
                    
    
#print(club_actuel())
            
def prem_selection():
    with open('output8.csv', 'r') as f:
            liste_selec = []
            spamreader = csv.reader(f)
            for i in spamreader:
                my_url = 'https://www.footballdatabase.eu/{}'.format("".join(i))
                opener = AppURLopener()
                response = opener.open(my_url)
                html_p = response.read()
                soup = BeautifulSoup(html_p, "lxml")
                inftech_club = soup.findAll("div", {"class":"player_technical"})
                for x in inftech_club:
                    contenu_club = x.findAll("div", {"class":"data"})
                    for j in contenu_club:
                        prem_selec = j.text
                        regex_selec = re.findall(r'Première sélection+.*', prem_selec)
                        for f in regex_selec:
                            liste_selec.append(f)
            return "\n".join(liste_selec)
#print(prem_selection())
