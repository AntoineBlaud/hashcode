# **NOTES HASHCODE** 

## Python


 #### Spécifier le type de l'argument et le type de retour
```
def function(var: int) -> int:
```

#### Méthodes spéciales utiles
```
__eq__()
__del__()
__repr__()
__str__()
__contains__()
__len__()
__add__()
__sub__()
__mul__()
```
 #### Sauvegarder ou copier un objet
```
import pickle
pickle.load()
pickle.dumps()

import copy
copy.deepcopy()
```
 #### Annotations 
```
@staticmethod
@property
```

#### Ajouter documentation
```
# Ici titre
def mafunction()
'''
Ici explication
'''
```

#### Decorateurs
```
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
decorate()
```


#### Générateurs
```
maliste = [a*2 for a in range(0,1000)]
mondic = {a:a*2 for a in range(0,1000)}
```

#### Exceptions
```
raise TypeError("Message")

# Gérer
try:
except ValueError:

# Bult-in: https://docs.python.org/3/library/exceptions.html
# Main: Exception

```
#### Trier ou melanger
```
Dict:  cT = dict(sorted(cT.items(), key=lambda t: t[1],reverse=True))
shuffle(DATA)

```
#### Thread et Multiprocessing
```
Thread: 
https://openclassrooms.com/fr/courses235344-apprenez-a-programmer-en-python/2235545-faites-de-la-programmation-parallele-avec-threading

import threading

def affiche(nb, nom = ''):
    for i in range(nb): print nom, i

a = threading.Thread(None, affiche, None, (200,), {'nom':'thread a'})
b = threading.Thread(None, affiche, None, (200,), {'nom':'thread b'})
a.start()
b.start()



Multiprocessing: 

p1 = multiprocessing.Process(target=self.glouton,args = (self.input_part1,"P1/",))
p2 = multiprocessing.Process(target=self.glouton,args = (self.input_part2,"P2/",))
p1.start()
p2.start()

```

#### Write same place in console
```
sys.stdout.write("Mon texte  \r")
sys.stdout.flush()
```
<br/>
<hr>

## C


#### Librairie JSON-C
```
DOC: https://json-c.github.io/json-c/json-c-0.10/doc/html/json__object_8h.html
https://progur.com/2018/12/how-to-parse-json-in-c.html

#include <json-c/json.h>
struct json_object *array;
parsed_json = json_tokener_parse();
json_object_get_string()
json_object_array_get_idx()
json_object_to_json_string()
json_object_new_array()
json_object_array_add()
json_object_array_length()
json_object_object_get_ex()
json_object_array_put_idx() 	
```
#### Clock
```
#include <time.h>

update = clock() + T_PRINT * CLOCKS_PER_SEC;
```

#### Files
```
# Know file size
f = fopen(json, "r");
fseek(f, 0, SEEK_END); // non-portable
int size = ftell(f);
buffer = (char *)malloc(sizeof(char) * size);
rewind(f);
fread(buffer, size, 1, f);

```
<br/>
<hr>

## Algorithmes

<br/>


#### Knuth-Morris-Pratt
Permet de rechercher des motis dans une chaîne de caractère
#### Rabin-karp
Hasher des données pour les comparer plus rapidement
#### Programmation dynamique TOP DOWN
Programmation récursive, enregistrer les résultats deja calculer
https://www.supinfo.com/cours/2ADS/chapitres/05-programmation-dynamique
#### Tri
Tri fusion, quicksort
#### Approche Gloutonne
L'approche gloutonne consiste à prendre le meilleur résulats à chaque étapes,
ce qui peut donner un bon résultat mais il ne sera pas parfait
<br>
<br>

#### Fenwick
Quand on travaille sur des intervalles on l'utilise, par exemple si on a une liste de client et qu'on souhaite savoir tout ce qui ont entre 100 et 1533 euros
#### Arbre intervalle
Permet de retrouver efficacement tous les intervalles qui chevauche un point ou un intervalle
#### Union-find
L'arbre se réagence sans cesse quand on fait une recherche afin d'avoir les données les plus recherché en premier
#### Chemin eurélien
Passer une fois par chaques routes
#### Poster chinois
Trouver le plus court chemin en passant au moins une fois par chaques routes
#### Voyageur de commerce
Plus court chemin en visitant chaque sommet une seule fois
#### Djikra
Plus court chemin, possibilité de négatif
#### Ford-fulkerson
Flot maximum, transport maximum                         
https://www.youtube.com/watch?v=eL3fTl4mykY
#### Algorithmes liens dansans: Knuth
Résoudre des problème de couverture exact; comme le sudoku
#### Merkle trees 
https://tryalgo.org/fr/2016/12/10/arbres-de-merkle/

#### Set cover et set packing
https://tryalgo.org/hashcode/

Soit un univers composé des entiers de 0 à n-1, ainsi qu’une liste d’ensembles sur cet univers. Dans le problème set cover il faut trouver une collection minimal d’ensembles qui couvrent tout l’univers. C’est-à-dire chaque entier de l’univers doit être contenu dans un ensemble de la solution. Dans la variante pondérée chaque ensemble vient avec un prix, et il faut minimiser le prix total de la solution.

Dans le problème set packing il faut trouver une collection d’ensembles disjoints, qui maximisent la taille de leur union. De manière équivalent on peut aussi chercher à minimiser le nombre d’éléments de l’univers pas couverts par la solution.

**Branch and Bound**


### Se renseigner sur : https://fr.wikipedia.org/wiki/21_problèmes_NP-complets_de_Karp
<hr>

## Etapes importantes 

 - Compréhension du problème
 - Analyse des fichiers (et des sous problèmes) + réflexion algorithmique
 - Récupération des données et organisation 
 - Conception de l'algorithme en essayant de le généraliser un maximum afin qu'avec de petites modifications il fonctionne sur tous les fichiers
 - Création de la visualisation , monitoring afin de surveiller la progression du score
 - Faire tourner l'algorithme en enregistrant les données dans des fichiers json
 - Finalement quand l'algo tourne, coder la sortie afin de soumettre le résultat

<hr>


## Others
Utiliser pypy

https://devdocs.io/numpy~1.17/routines.ctypeslib#numpy.ctypeslib.as_ctypes

https://stackoverflow.com/questions/22425921pass-a-2d-numpy-array-to-c-using-ctypes/27737099

https://stackoverflow.com/questions/4145775/how-do-i-convert-a-python-list-into-a-c-array-by-using-ctypes

https://stackoverflow.com/questions/4355524/getting-data-from-ctypes-array-into-numpy

https://towardsdatascience.com/an-introduction-to-gpu-optimization-6ea255ef6360

https://www.journaldev.com/31907/calling-c-functions-from-python

https://www.csestack.org/calling-c-functions-from-python/

https://docs.python.org/2/library/ctypes.html

## Install pypy 

sudo wget https://bootstrap.pypa.io/get-pip.py 
sudo pypy3 -m venv myvenv --without-pip --system-site-packages  
python3 -m venv myvenv --without-pip --system-site-packages 
pypy3 -m ensurepip         
pypy3 get-pip.py    
sudo apt-get install python3.6-venv    
sudo add-apt-repository ppa:pypy/ppa   
sudo apt update 
sudo apt install pypy3  
wget https://bootstrap.pypa.io/get-pip.py
./pypy get-pip.py

For usage try,
pypy -m pip install validators

