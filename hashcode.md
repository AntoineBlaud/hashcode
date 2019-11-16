# **NOTES HASHCODE** 

## Python

<br/>

 ### Spécifier le type de l'argument et le type de retour
```
def function(var: int) -> int:
```

### Méthodes spéciales utiles
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
 ### Sauvegarder ou copier un objet
```
import pickle
pickle.load()
pickle.dumps()

import copy
copy.deepcopy()
```
 ### Annotations 
```
@staticmethod
@property
```

### Ajouter documentation
```
# Ici titre
def mafunction()
'''
Ici explication
'''
```

### Decorateurs
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


### Générateurs
```
maliste = [a*2 for a in range(0,1000)]
mondic = {a:a*2 for a in range(0,1000)}
```

### Exceptions
```
raise TypeError("Message")

# Gérer
try:
except ValueError:

# Bult-in: https://docs.python.org/3/library/exceptions.html
# Main: Exception

```
### Trier ou melanger
```
Dict:  cT = dict(sorted(cT.items(), key=lambda t: t[1],reverse=True))
shuffle(DATA)

```
### Thread et Multiprocessing
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

### Write same place in console
```
sys.stdout.write("Mon texte  \r")
sys.stdout.flush()
```
<br/>

## C

<br/>

### Librairie JSON-C
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
### Clock
```
#include <time.h>

update = clock() + T_PRINT * CLOCKS_PER_SEC;
```

### Files
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
Plus court chemin
#### Ford-fulkerson
Flot maximum, transport maximum                         
https://www.youtube.com/watch?v=eL3fTl4mykY


