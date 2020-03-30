from urllib.request import urlopen as uopen
from bs4 import BeautifulSoup
import re
#import pandas as pd

def resMatch():
    output = []
    my_url = uopen('https://www.matchendirect.fr/espagne')
    html_p = my_url.read()
    my_url.close()
    soup = BeautifulSoup(html_p, "html.parser")
    container = soup.findAll("div", {"id":"livescore"})
    for c in container:
        team_c = c.findAll("td", {"class":"lm3"})
        for x in team_c:
            team = x.a["title"]
            regex_team = re.findall(r'[^Détail du match \:].*', team)
            score_c = x.findAll("span", {"class":"lm3_score"})
            score = score_c[0].text
            output.append("".join(regex_team))
            
    return output
#            print("MATCH:" + "\t" +  team)
#            print("SCORE:" + "\t" + score)
print(resMatch())


def score():
    output_score = []
    my_url2 = uopen('https://www.matchendirect.fr/espagne')
    html_p2 = my_url2.read()
    my_url2.close()
    soup2 = BeautifulSoup(html_p2, "html.parser")
    container_score = soup2.findAll("div", {"id":"livescore"})
    for con in container_score:
        team_con = con.findAll("td", {"class":"lm3"})
        for x in team_con:
            score_c = x.findAll("span", {"class":"lm3_score"})
            score = score_c[0].text
            output_score.append(score)
    return output_score
#print(score())
    
def statut():
    output_statut = []
    my_url3 = uopen('https://www.matchendirect.fr/espagne')
    html_p3 = my_url3.read()
    my_url3.close()
    soup3 = BeautifulSoup(html_p3, "html.parser")
    container_statut = soup3.findAll("div", {"id":"livescore"})
    for cont in container_statut:
        team_cont = cont.findAll("td", {"class":"lm2 lm2_0"})
        for x in team_cont:
           
            statut_c = x.span.decompose()
            statut = x.text
            output_statut.append(statut)
    return output_statut

#print(statut())


def horaire():
    output_horaire = []
    my_url3 = uopen('https://www.matchendirect.fr/espagne')
    html_p3 = my_url3.read()
    my_url3.close()
    soup3 = BeautifulSoup(html_p3, "html.parser")
    container_statut = soup3.findAll("div", {"id":"livescore"})
    for cont in container_statut:
        team_cont = cont.findAll("td", {"class":"lm2 lm2_0"})
        for x in team_cont:
            horaire = x.next_element.text.strip("-- :&nbsp--")
            output_horaire.append(horaire)
#            print(output_horaire)
    return output_horaire

#print(horaire())
