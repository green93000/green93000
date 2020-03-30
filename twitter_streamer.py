import tweepy
import re
from tweepy import OAuthHandler

## informations : mon compte twitter
## la clef et les tokens
consumer_key="y5gXigsgFFUIPaaJVQ0WqsdUN"
consumer_secret="hxbf0pnmDmHqJN8itvQm2MsmHXhm5QvB8u87PLEzvw5oBZVMr2"
access_token="1228255293345234945-Eblm8PkYNa1Qxx2BbvT9vCB7l96qbp"
access_token_secret="Lj2KD7PqXi5pXSF8J1MVu2dhilJkdHgfAwDaG1KB8d7LG"

## identification : utiliser mon  compte
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## Ouvrir mon fichier pour exporter les tweets. Il faut le mettre dans le répertoire actuel.
# Si ce fichier n'existe pas, je le crée dans le répertoire actuel.
export=open("export_tweets.txt",mode="w",encoding="utf-8")

## Choisir la langue
language=input("select a language (fr for french, all for all languages)>> ")

## Sélectionner une date

# Date supérieure à :
#date_from=input("select date  : from YYYY-MM-DD ")

# Date inférieure à :
#date_to=input("               :  to  YYYY-MM-DD ")


# Ouvrir le fichier contenant les noms d'utilisateur twitter (screen names) 
accounts_file=open("AccountsList.txt",mode="r",encoding="utf-8")
# Lecture du fichier en question
read_file=accounts_file.read()
# Parcourir le fichier et créer une liste dans laquelle on met les noms d'utilisateur
# Utiliser le marqueur \n (ligne) pour récupérer les noms d'utilisateur
users=read_file.split("\n")

## Parcourir la liste et stocker à chaque tour un nom d'utilisateur dans la variable "user"

for user in users:
	# On peut définir une date et le nombre de tweets que l'on veut récupérer par utilisateur
	#f=api.user_timeline(user,since=date_from,untill=date_to,count=1000)

	# En parcourant la liste, on risque de trouver un caractère qui ne correspond pas à un compte twitter
	# On fait donc une condition : le nom récupéré ne sera traité que s'il correspond à un nom d'utilisateur
	if user != "":
		# On connecte le nom d'utilisateur à l'api tweepy 
		# On récupère 500 tweets de l'utilisateur dans la variable "user"
		try:
			f=api.user_timeline(user,count=1000,tweet_mode="extended")
			## On sélectionne les tweets par langue : fr pour français et all pour toutes les langues
			for k in f:
				if language==k.lang:
					# On récupère le contenu textuel
					# On affiche les tweets sur le terminal (encodage utf-8)
					dt= k.full_text.encode("utf-8")
					print (dt)
					## données : métainformations liées à un tweet (date) et le texte du tweet
					author_n=k.author.name
					data=("Author = "+str(author_n)+"\t"+str("Date = "+str(k.created_at))+"\t"+str("tweet = "+str(k.full_text))+"\n")
					# on peut récupérer les retweets de l'utilisateur
					ret=k.retweeted
					export.write(data)
					##print (str("---------------"+str(ret)))
				elif language =='all':
					dt= k.full_text.encode("utf-8")
					print (dt)
					## données : métainformations liées à un tweet (date) + le texte du tweet
					author_n=k.author.name
					data=("Author = "+str(author_n)+"\t"+str("Date = "+str(k.created_at))+"\t"+str("tweet = "+str(k.full_text))+"\n")
					# on peut récupérer les retweets de l'utilisateur
					ret=k.retweeted				
					export.write(data)
					##print ("-------",k.retweeted)
		except:
			continue
export.close()
accounts_file.close()
print("\n\n"+"End"+"\n")

usr=input("To stop the program enter stop : ")
while usr == "stop":
	break