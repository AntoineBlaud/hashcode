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

#### Write same place in console
```
sys.stdout.write("Mon texte  \r")
sys.stdout.flush()
```
#### Autres
```
Savoir utiliser:
set()
map()
lambda
zip()
enumerate()
extend()
filter()
f.readline().strip().split(" ")
```

### Numpy (ne pas utiliser)
```
https://numpy.org/doc/1.17/reference/routines.html
https://numpy.org/doc/1.17/reference/routines.array-creation.html
https://numpy.org/doc/1.17/reference/routines.array-manipulation.html
```
<hr>

### Speed up code

#### Thread et Multiprocessing
```
"Threading: 
https://openclassrooms.com/fr/courses235344-apprenez-a-programmer-en-python/2235545-faites-de-la-programmation-parallele-avec-threading
https://sebastianraschka.com/Articles/2014_multiprocessing.html
https://www.ellicium.com/python-multiprocessing-pool-process/

import threading

def affiche(nb, nom = ''):
    for i in range(nb): print nom, i

a = threading.Thread(None, affiche, None, (200,), {'nom':'thread a'})
b = threading.Thread(None, affiche, None, (200,), {'nom':'thread b'})
a.start()
b.start()

#Multiprocessing: 
p1 = multiprocessing.Process(target=self.glouton,args = (self.input_part1,"P1/",))
p2 = multiprocessing.Process(target=self.glouton,args = (self.input_part2,"P2/",))
p1.start()
p2.start()

```


#### line_profiler
```
import line_profiler
import atexit
profile = line_profiler.LineProfiler()
atexit.register(profile.print_stats)

mettre @profile devant fonction
```

#### Memory usage
```
from guppy import hpy; h=hpy()
h.heap()
```
#### Numba (ne pas utiliser )
```
from numba.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings
from numba import *

warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

mettre @jit(nopython=True,parallel=True) devant fonction

```

#### Conseils
```
Utiliser pypy !!!
10**10 itérations environ 10 minutes avec pypy et 40 avec python3

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

**Choisir entre** :
- glouton
- dynamique
- pulp
- branch and bound


<br/>
<hr>

#### Knuth-Morris-Pratt
Permet de rechercher des motis dans une chaîne de caractère
#### Rabin-karp
Hasher des données pour les comparer plus rapidement
#### Programmation dynamique TOP DOWN
Programmation récursive, enregistrer les résultats deja calculer
https://www.supinfo.com/cours/2ADS/chapitres/05-programmation-dynamique
#### Tries
Tri fusion, quicksort
#### Approche Gloutonne
L'approche gloutonne consiste à prendre le meilleur résulats à chaque étapes,ce qui peut donner un bon résultat mais il ne sera pas parfait
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
#### Algorithmes génétiques
https://antoinevastel.com/algorithme/python/algorithmes%20g%C3%A9n%C3%A9tiques/2016/04/30/probleme-voyageur-commerce.html
#### Linear programming
https://towardsdatascience.com/linear-programming-and-discrete-optimization-with-python-using-pulp-449f3c5f6e99

https://buildmedia.readthedocs.org/media/pdf/python-mip/latest/python-mip.pdf

http://benalexkeen.com/linear-programming-with-python-and-pulp/

https://www.linkedin.com/pulse/bin-packing-python-pulp-michael-basilyan

https://coin-or.github.io/pulp/CaseStudies/a_blending_problem.html#

https://pyomocontrib-simplemodel.readthedocs.io/en/latest/knapsack.html

https://pythonhosted.org/PuLP/CaseStudies/a_sudoku_problem.html
#### Merkle trees 
https://tryalgo.org/fr/2016/12/10/arbres-de-merkle/
#### Branch and Bound
https://www.youtube.com/watch?v=3RBNPc0_Q6g
https://www.youtube.com/watch?v=1FEP_sNb62k
https://www.youtube.com/watch?v=yV1d-b_NeK8

http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/specials/algorithm_culture.html

<hr>

## Etapes importantes 

 - Compréhension du problème
 - Analyse des fichiers (et des sous problèmes) + réflexion algorithmique
 - Récupération des données et organisation 
 - Conception de l'algorithme en essayant de le généraliser un maximum afin qu'avec de petites modifications il fonctionne sur tous les fichiers
 - Savoir subdiviser le problème correctement
 - Création de la visualisation et monitoring afin de surveiller la progression du score
 - Optimiser à l'aide du profiler
 - Faire tourner l'algorithme en enregistrant les données dans des fichiers json
 - Coder la sortie afin de soumettre le résultat

 *Optimser pour pypy, si tableau totalement statique passer à numpy*

<hr>


## Others

https://devdocs.io/numpy~1.17/routines.ctypeslib#numpy.ctypeslib.as_ctypes

https://stackoverflow.com/questions/22425921pass-a-2d-numpy-array-to-c-using-ctypes/27737099

https://stackoverflow.com/questions/4145775/how-do-i-convert-a-python-list-into-a-c-array-by-using-ctypes

https://stackoverflow.com/questions/4355524/getting-data-from-ctypes-array-into-numpy

https://towardsdatascience.com/an-introduction-to-gpu-optimization-6ea255ef6360

https://www.journaldev.com/31907/calling-c-functions-from-python

https://www.csestack.org/calling-c-functions-from-python/

https://docs.python.org/2/library/ctypes.html

<hr>



## 21 Problèmes combinatoires

- **SAT** : *Un problème de ce type consiste a satisfaire un ensemble de condition (et, ou, not) de manière a vérifier si il peut  y avoir un résultat juste/possible . On modélise le problème par des variables Xijz par exemple avec i la valeur et jz la position, puis on ecrit les conditions et on trouve les valeurs*


    Exemple d'application: *Emploi du temps, les 4 reines.*

    Algorithme de résolution: *https://fr.wikipedia.org/wiki/Algorithme_DPLL*; 
    https://github.com/jcwleo/DPLL-Algorithm/blob/master/DPLL.py

    Liens: *http://monge.univ-mlv.fr/~thapper/teaching/mmpo/2017/05-slides.pdf* ; *http://igm.univ-mlv.fr/~thapper/teaching/mmpo/2017/06-slides.pdf*


- **CLIQUE** : *Trouver dans un graphe le plus grand réseau de noeud qui sont tous connecté les uns aux autres, par exemple trouver le plus grand groupe de personne qui se connaissent toutes*

    Liens: *https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_la_clique*

    Algorithmes: https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm ; https://iq.opengenus.org/bron-kerbosch-algorithm/

- **SET PACKING** : *Soit un univers U et S1,...,Sn une liste d'ensemble. Le but est de trouver une collection d'ensemble disjoint(min ou max) qui maximisent la taille de leur union*

    Exemple d'application: Pizza hashcode

    Algorithmes: https://tryalgo.org/fr/2017/01/22/google-hashcode-google-pizza/

- **VERTEX COVER**: *Le but est de trouver le minimum de sommet qui réunisse toutes les branches*

    Algorithmes: Calculer couplage maximal: https://fr.wikipedia.org/wiki/Couplage_(th%C3%A9orie_des_graphes)

- **SET COVERING**: *Le but est de couvrir tout univers U avec des sous ensembles S telles que le coût soit minimal(chaque ensemble S à un côut)*

    Algorithme: https://www.emse.fr/~delorme/Papiers/MemoireDEA/memoire004.html

- **FEEDBACK ARC-NODE SET**: *Supprimer des noeuds ou des branches afin de rendre le graphe acyclique*

- **HAMILTONIEN** : *Dans un graphe trouver un chemin qui passe une et une seule fois par chaque sommet*

    De même:

    - **Chemin eurélien**:
    Passer une fois par chaques routes
    - **Poster chinois**:
    Trouver le plus court chemin en passant au moins une fois par chaques routes https://www.me.utexas.edu/~jensen/ORMM/supplements/units/net_methods/rel_net_lp.pdf
    http://home.ubalt.edu/ntsbarsh/opre640A/partIII.htm#rsppr
    - **Voyageur de commerce**:
    Plus court chemin en visitant chaque sommet une seule fois
    - **Djikra**:
    Plus court chemin, possibilité de négatif
    http://home.ubalt.edu/ntsbarsh/opre640A/partIII.htm#rsppr

- **EXACT COVER**: Étant donné un ensemble U et une collection S  de sous-ensembles de U, une couverture exacte de U est une sous-collection S ∗  de S tel que tout élément de U est élément d'exactement un des ensembles de S ∗ En d'autres termes, une couverture exacte de U est une sous-collection S ∗  de S qui est une partition de U : les ensembles éléments de S ∗  sont disjoints deux à deux, et leur union est U. 

    Exemple d'application: Les 8 dames, sudoku

    Algorithmes: Programmation dynamique ou X knuth

    Liens: https://fr.wikipedia.org/wiki/Algorithme_X_de_Knuth

- **ARBRE DE STEINER**: *Trouver l'arbre minimal qui regroupe tous les noeuds*

    Algoithme: https://fr.wikipedia.org/wiki/Algorithme_de_Kruskal

- **HITTING SET**: *Étant donné une famille S de sous-ensembles d'un « univers » U, on cherche un sous-ensemble H de U (le hitting set) qui contient au moins un élément de chaque sous-ensemble de la famille S. De plus, il est demandé que le nombre d'éléments de H n'excède pas une valeur k donnée.*

    Algorithmes: https://www.analyticsvidhya.com/blog/2017/02/lintroductory-guide-on-linear-programming-explained-in-simple-english/

- **KNAPSTACK**: *Le problème du sac à dos* (fait)

    Algorithmes: programation dynamique(résolution exact), glouton, génétique, 

- **JOB SEQUENCING**: *Un ensemble de taches avec des durées d'execution et des pénalités* (fait)

- **PARTITION**: *Soit S un multiensemble d'entier naturel, on veut vérifier si il exsite une parition de S telle que la somme des éléments de S1 soit égale à celle de S2*


#### Bases

```
import sys
import os
import time
import argparse
import re
from copy import copy
import pulp
from functools import reduce
import pickle
import multiprocessing
import numpy as np
import random
import matplotlib.pyplot as plt
import datetime
import tqdm
######################################################################################
import line_profiler
import atexit
profile = line_profiler.LineProfiler()
atexit.register(profile.print_stats)
######################################################################################




if __name__ == '__main__':

    DEFAULT_F = ""
    OUTPUT_F = ""

    parser = argparse.ArgumentParser(description='Compute hashcode pizza regina')
    parser.add_argument('-i', '--filein', help='Input file',default=DEFAULT_F, type=str)
    parser.add_argument('-o', '--fileout', help='Ouput file',default=OUTPUT_F, type=str)
    parser.add_argument('-v', '--verbose', default=-1,help='verbose mode', type=int)
    args = parser.parse_args()

   


```
