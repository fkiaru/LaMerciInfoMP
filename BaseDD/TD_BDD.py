#############
### MISE EN ROUTE
#############

import sqlite3

## Creation d'une connection
connection = sqlite3.connect("chinook.db")
cursor=connection.cursor()
def sql(od):
    res = cursor.execute(od).fetchall()
    return res

################
##   EXEMPLES
################

## Affichage la liste de toutes les tables
TABLELIST = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print(list(map(lambda x: x[0],TABLELIST))) # fonction map(func, iterables)


# Donner la liste de tous les genres musicaux.
sql('SELECT Name FROM genres') # c'est une projection

# Sélectionner les lignes de la table genres dont le Name de Genre comme par la lettre E
sql("SELECT * FROM genres WHERE Name LIKE 'E%'")

# Donner le nom des musiques dont le nom du compositeur se termine par la lettre x
sql("SELECT Name,Composer FROM tracks WHERE Composer LIKE '%x'")

# Donner pour chaque musique : son nom et sa durée en minutes, affiché avec des virgules
sql('SELECT Name, milliseconds/60000. FROM tracks')

############################
## NIVEAU 1
############################
# Donner la liste des noms de playlists

# Donner le nombre de genres de musiques de noms différents

# Donner la liste des fonctions (title) des employees

# Donner, par ordre alphabétique, la liste des Pays dont viennent les clients,

############################
## NIVEAU II
############################
# Donner le nom des artistes commençant par la lettre R triée par ordre alphabétique

## Donner le nom de musiques en face du nom de chaque playlists

# Donnner le nombre de musiques dont la durée dépasse 15 min 

# Donner la liste des noms de compositeurs de la playlist "Movies" 
# dont le nom contient le groupe de lettres "ichael", la liste
# devant être triée par ordre alphabétique

# lister tous les genres musicaux différents contenus dans la playlist appelée "Classical"


# Lister toutes les noms de musiques du genre "Reggae" précédées du nom de l'album
# Les résultats doivent être triés par ordre alphabétique d'album

############################
## NIVEAU III
############################
# Combien y a-t-il d'artistes différents dans la playlist "Brazilian Music"


# Donner, pour chaque playlist sa durée totale en heures


# Donner le nombre de musiques de chaque genres parmi les musiques de la table tracks
# On triera les données par ordre alphabétique de genre

# Donner, pour chaque genre musical, le nombre d'artistes parmi les musiques de la table tracks

## Donner les noms des cinq morceaux les plus longs en durée de la playlist 'Music'

# Quel est, pour chaque playlist, la durée du morceau le plus long?

############################
## NIVEAU IV
############################

## Donner l'artiste le plus représenté dans chaque genre musical
## parmi les musiques de la liste tracks

# Quel est, pour chaque playlist, le nom du morceau le plus long et sa durée en minutes


## Donner le compositeur le plus présent pour chaque playlist, 
## en cas d'égalité on souhaite que ce soit le compositeur dont le
## est le premier dans l'ordre alphabétique qui soit utilisé


## Question subsidiare: afficher en plus la fréquence 
## maxi de ce compositeur
# on fait une table avec la fréquence maxi du composer



