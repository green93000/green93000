from bs4 import BeautifulSoup
import urllib.request
import re

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open('https://www.footballdatabase.eu/fr/joueur/details/10973-lionel-messi')
html_p = response.read()

soup = BeautifulSoup(html_p, "html.parser")

#Joueurs

def joueurs():
    liste = []
    container = soup.findAll("div", {"class":"player"})
    print("JOUEURS ACTUELS:" + "\n")
    for c in container:
            player_c = c.findAll("h3", {"class":"name"})
            player = player_c[0].a.text
            liste.append(player)
    return liste

#Nom du club
    
def club_info():
    liste_club = []
    container2 = soup.findAll("div", {"class":"techpage"})
    for x in container2:
        acc = x.findAll("div", {"class":"technical"})
        titre = acc[0].h1.text
        liste_club.append(titre)
    return "\n".join(liste_club)


#Dernier match joué
    
def DernMatch():
    liste_match = []
    container3 = soup.findAll("div", {"class":"module results club"})
    for i in container3:
        comp1_c = i.findAll("div", {"class":"fullresult"})
        comp1 = comp1_c[0].h3.a.text
    container4 = soup.findAll("div", {"id":"full_in_0"})
    for y in container4:
        club_vic = y.findAll("div", {"class":"firstclub vic"})
        club_perd = y.findAll("div", {"class":"secondclub los"})
        date_c = y.findAll("div", {"class":"date"})
        score_vic = y.findAll("span", {"class":"first_score vic"})
        score_los = y.findAll("span", {"class":"second_score los"})
        club1 = club_vic[0].a.text
        club2 = club_perd[0].a.text
        date = date_c[0].text
        first_score = score_vic[0].text
        second_score = score_los[0].text
        liste_match.append(comp1 + ": " + "\t" + club1 + "\t" + first_score + " - " + second_score + "\t" + club2)
        liste_match.append("\n" + date)
    return "".join(liste_match)


        
    


