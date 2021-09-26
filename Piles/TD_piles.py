## Exercice palindrome

def estPalindrome(s):
 '''
    entrée: s  = chaîne de caractère
               = mot à analyser
    sortie: booléen = Vrai si s est un palindrome
    '''

... # à compléter

# Script de validation de la fonction estPalindrome
# on utilise des mots avec un nombre de lettres qui est pair et impair

listeTest=['radar','été','math','erre','maths']
for mot in listeTest:
    print(mot,'\t',estPalindrome(mot))

## Exercice : notation polonaise inversée

def evalueNP2(expr): # à compléter


# Validation de la fonction à l'aide de 4 expressions
E1=[4,5,'+']
E2=[24,4,"-",4,"*",11,3,"/","+"]
E3=[3,4,7,"+","*"]
E4=[4,7,"+",3,"*"]
listExp=[E1,E2,E3,E4]
for exp in listExp:
    print(exp,'valeur = ',evaluateNPI(exp))


## Exercice : mélange de cartes
# indication on utilisera la fonction randrande
from random import randrange
help(randrange)

## 1ere partie : fonction coupe paquet

def coupe(paquet):
    '''Entrée: paquet est une pile d'entiers de n éléments
    Sortie : la pile initiale à laquelle on a retiré entre 1 et n-1 éléments
    et la pile des éléments retirés, dans le même ordre que la pile initiale'''
# à compléter

# Validation de la fonction coupe
paq1 = [k for k in range(12)]
paq2 = coupe(paq1)
print(paq1)
print(paq2)

## 2ème partie 
def melange(paquet1, paquet2) :
    ''' Principe : on initialise une pile VIDE.
    ON boucle tant que paquet1 et paquet2 sont non vides, 
    tirer au hasard un des paquets
    empiler la carte du dessus dans la pile résultat.
    Dès qu'un des paquets est vide, vide le plein dans le résulat.'''
# à compléter

#Validation du mélange
paq1=[k for k in range(12)]
paq2=coupe(paq1)
print(paq1,paq2)
paq3=melange(paq1,paq2)
print(paq3)
print(paq1,paq2)

## Exercice : Empiler, dépiler, rempiler, ...
def renverse(p):
# à compléter


# validation 
p1 = [k for k in range(10)]
print(p1)
print(renverse(p1))
print(p1) # p1 est vidée après l'opération

## Accès à un élément par son indice
def renvoie1(p,n) :
    ''' Principe, on utilise une pile auxiliaire qui sert 
    à stocker les n valeurs renversées puis on reconstitue toute la pile
    en dépilant à noueau la pile auxilaire dans la pile initiale'''

# validation
P1 = [k for k in range(11)]
print(renvoie1(P1,0))
print(P1)

## Mise au fond
def top2groud(p):
    '''Principe : on stocke le 1er élément, on dépile tout, on empile le 1er élément
    On réempile tout'''
# à compléter

# validation
p0 = [k for k in range(10)]
print('AVANT',p0)
top2groud(p0)
print('APRES',p0)


## Projet labyrinthe parfait

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
#construction d'un labyrinthe parfait
n = 35
atteinte = [[False] * n for i in range(n)]
def visiter(c): # écrit la case c comme atteinte.
    (x,y) = c
    if x<0 or x>=n or y<0 or y>=n:
        return # on sort de la fonction
    atteinte[x][y] = True
    
def est_atteinte(c): # donne l'état (atteinte ou non) de la case c.
    (x,y) = c
    if x<0 or x>=n or y<0 or y>=n:
        return True
    return atteinte[x][y]

def choix(c):
    (x,y)=c
    r=[]
    def ajouter(p):
        if not est_atteinte(p): 
            r.append(p)
    ajouter ((x-1,y))
    ajouter ((x+1,y))
    ajouter ((x,y-1))
    ajouter ((x,y+1))
    return r

def tirage(L):
    n=len(L)
    assert n>0
    return L[np.random.randint(0,n)]

def labyrinthe():
    # pile = creer pile # A MODIFIER
    # pile =  empile(pile,(0,0))# A MODIFIER
    visiter((0,0)) 
    while not pile# est_vide(pile) : A MODIFIER
        cellule# = dépiler(piler)
        c = choix(cellule)
        if len(c)>0:
            suivante=tirage(c)
            # relier les cases cellulee et suivante
            # A COMPLETER
            # ...
            visiter(suivante)
             # empiler(pile,cellue) A MODIFIER
             # empiler(pile,suivante) A MODIFIER

image0 = np.zeros((#,#, 3), dtype=np.uint8) # A COMPLETER 
labyrinthe()
plt.imshow(image0)
plt.axis('off')
mpimg.imsave("laby1.png",image0)