## EXERCICE 1 : FONCTION FACTORIELLE

def fac(n) : # version récursive


# Validation 5! = 120 ?
print(fac(5))

## 
def facIter(n) :  # version itérative de factorielle

print(facIter(5))

# COMPARER LES COMPLEXITES

## 
def factTerm(n, res = 1) # version en récursivité terminale de la factorielle

## EXERCICE 2 : RECURSIVITE MUTUELLE

# Recursivité mutuelle
def suiteU(n):

def suiteV(n):

## EXERCICE 3: suite de Fibonacci

def fibo(n): # version récursive

for k in range(16):
    print(k,fibo(k))

## 
def fiboIter(n) : # version itérative


for k in range(16):
    print(k,fiboIter(k))

## Exercice 3 : le flocon de Koch

# CODE à compléter
import turtle # module turtle
def koch(a, n):
    if n == 0: # condition d'arret
        t.forward(a)
        return
    # à compléter
    #
    #
    
# SCRIPT D'APPEL A LA FONCTION
turtle.TurtleScreen._RUNNING = True
w = turtle.Screen()

w.setup(1400, 700) # taille de la zone de tracée (PIXELS_X, PIXELS_Y)
w.clear()
w.visible = True
t = turtle.Turtle()
t.speed("fastest") # ou bien nombre entier entre 1 (lent) et 10 (rapide), zéro.
t.up()
t.setpos(-600, -200) # position initiale de la tortue
t.down()
koch(1200,1) # APPEL A LA FONCTION KOCH
w.exitonclick()

## EXERCICE 4 : recherche d'un élément dans une liste triée

def dansListe(L, x) : # recherche dichotomique dans une liste triée à compléter
    n = len(L)
    if n == 0 :
        # à compléter
    m = # "milieu" de la liste
   
    if  # élémet trouvé à l'indice m
        return True
    elif # condition de dichotomie    
         # recherche dans la sous-liste de drotie
        return dansListe(L[## ], x) #slicing
    else : # sous liste de 'gauche'
        return dansListe(L[##], x) #slicing

# CODE DE VALIDATION
L0 = [ 2*k+1 for k in range(int(2e4)) if k %17 == 0 or k %3 == 0]
xListe = [561, 12409, 17471, 22501, 39997]
print('len(L0) = ',len(L0))
for x in xListe:
    nbAppel=0
    dans = dansListe(L0,x)
    print(dans, nbAppel)

## Exercice 5 : Triangle de Pascal et ensemble des parties d'un ensemble

def C(k,n):
    if (k < 0) or (k > n): # k doit être compris entre 0 et n au sens large
        # A COMPLETER
        return ...
    if (n == 1): # pour un ensemble à 1 élément, il n'y a une manière 
                #unique de construire les parties (à zéro ou 1 élément)
        return ...
    return ...

# COMPARAISON AVEC L'EXPRESSION N!/((N-k)!k!)
print(C(5,11))
print(fac(11)/((fac(5)*fac(11-5))))

## ENSEMBLE DES PARTIES D'UN ENSEMBLE A k éléments
def parties(L,k): # ensemble des parties à k éléments de l'ensemble L

# VALIDATION
N = 4 # ensemble à 4 éléments
L0 = [j for j in range(N)]
for k in range(N + 1):
    ensParties = parties(L0,k)
    print('k=', k,' nb = ', len(ensParties), C(k,N))
    print(ensParties)

## Ensemble des parties d'un ensemble
def ensPartieTotal(L): # ensemble des parties de l'ensemble L (récursivité)
    if # condition d'arrêt
        return ## ensemble ne contenant que l'ensemble vide...
    res = # appel récursif pour déterminer P
    if len(res)>0 : # ajout du dernier élément à P
        for el in res :
            ## à compléter
    return ## à compléter

# Validation
L0 = ['a','b','c','d']
rr=ensPartieTotal(L0)
#print(rr)
print(rr)
print('Card(Ensemble des Parties) = ',len(rr))

##  Exercice 6 : Ensemble des permutations

# Pour un ensemble à 3 éléments
L0=['a','b','c']
nbCall=0
res=perm1(L0)
print(res)
print(len(res),nbCall)
print(nbCall/len(res))

## EXERCICE 7 : combinaisons d'entiers

def getCombinaisons(n): # version récursive

# Validation du programme
for k in range(1,5):
    res = getCombinaisons(k)
    print(k,res)

## EXERCICE 8 : tri récursif par insertion
def triRecInsert(L): # tri récursif par insertion
    n = len(L)
    if # condition d'arrêt
        return L
    Lsub = # sous-liste triée des n-1 éléments restants
    for k in range(n-1): # recherche d'une position d'insertion
        if L[0] < Lsub[k]: # condition d'insertion
            return # insertion à l'emplacement k par concaténation
    return  #cas où l'élément est inséré en fin de liste
# Validation

L0 = [1,-3,2,91,4,5,8,-12,102,43,28,32,-1000,4,5,18]
res = triRecInsert(L0)
print(res)

# application pour une matrice aléatoire
import numpy as np
M=np.random.rand(5,10)
n,m=np.shape(M)
for k in range(m):
    L0=M[:,k]
    L0=L0.tolist()
    La=L0.copy()
    La.sort()
    if La==triRecInsert(L0):
        print('ok')
    else:
        print('!')
 

## Exercice 9 : Exponentiation et exponentiation rapide
def puissance1(a,n):
    """Fonction récursive qui calcule a^n:
    entrées : a, nombre réel, n nombre entier naturel
    sorties : a^n    """
    if n==0 :
        return 1
    return a*puissance1(a,n-1)

## 
def puissanceTerm(a, n, res = 1): # version récursivité terminale
    if : # condition d'arrêt
        return #
    return # à compléter
# validation
print(puissanceTerm(2,5))
print(puissanceTerm(3,0))
somme=0
for k in range(10):
    somme += puissanceTerm(3,k)
print(somme)    

## Exponentiation rapide récursive
def puissanceRapide(a,n): # exponentiation rapide récursive

# validation
print(puissanceRapide(3,128))
print(3**128)

## Exponentiation rapide en récursivité terminale

def puissanceRapideTermAux(a,n): # n doit être une puissance de 2
    
# validation
for k in range(8): # VALIDATION
    print(3**k,puissanceRapideTerm(3,k))

## cas quelconque
def puissanceRapideTerm(a,n,res=1): # exponentiation rapide en récursivité terminale
    if n ==0 : # condition d'arrêt N°1
        
    if n ==1 : # condition d'arrêt N°2
        
        return a* res # la variable res est prise en compte à la fin
    if (n % 2 == 0): # parité?
        return  # n pair
    else:
        return # n impair

## déréursivation
def puissanceIterRapide(a,n): # exponentiation rapide dérécursivée

#validation
for k in range(12):
    print('3 ^( ',k,' ) = ',3**k,'  ', puissanceIterRapide(3,k))

## Exercice 10 : les tours de Hanoï
# TRAME A COMPLETER
def deplacer(n,i,f):
    if ... :
        inter = ...
        deplacer(..., ..., ...)
        print( .. ,' --> ',...)
        deplacer(...,...,...)
#validation (à compléter)