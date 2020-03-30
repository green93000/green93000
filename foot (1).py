
# coding: utf-8

# In[3]:



import re

# TRAITEMENT DU FICHIER

## ouvrir un fichier
fichier = open("export_tweets.txt", "r")
print (fichier)
content = fichier.read()
mots = content.split()
print (content)
fichier.close()


# In[4]:


manchester = ["Mohamed Salah,Sadio Mané,Alisson Becke,Takumi Minamin,Virgil van Dijk,Roberto Firmino,Jordan Henderson,Trent Alexander-Arnold,Naby Laye Keïta,Fabinho,James Milner,Curtis Jones,Alex Oxlade-Chamberlain,Xherdan Shaqiri,Andrew Robertson"]
liverpool = ['Dejan Lovren','Nathaniel Phillips']
for joueur in content:
    if joueur in manchester:
        print(joueur,"joueur de manchester")
    elif joueur in liverpool:
        print(joueur,"joueur de liverpool")
    else:
        print(joueur, "inconnu")

