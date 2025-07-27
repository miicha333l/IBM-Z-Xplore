# Défi CODE1 – Premiers pas en Python sur IBM Z

Ce dossier contient les fichiers et explications pour le défi CODE1 de la plateforme IBM Z Xplore.

## Objectif
Découvrir les bases du langage Python sur z/OS : variables, boucles, conditions, exécution de scripts.

## Fichiers principaux
- `code1.py` : Script Python de base à exécuter et analyser.
- `code2.py` : Script pour expérimenter les variables et conditions.
- `marbles.py` : Script pour manipuler les boucles et la logique.

## Étapes du défi
1. Copier les scripts depuis `/z/public` si besoin :
   ```sh
   cp /z/public/code1.py ~
   cp /z/public/code2.py ~
   cp /z/public/marbles.py ~
   ```
2. Exécuter un script :
   ```sh
   python3 code1.py
   ```
3. Modifier, tester, et explorer le code dans VS Code ou via le shell USS.

## Ressources utiles
- [Documentation Python](https://docs.python.org/fr/3/)
- [IBM Z Xplore](https://ibmzxplore.influitive.com/)

## Exemples de code Python

### Compter à rebours
```python
import time
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
print("Décollage !")
```

### Vérifier la présence d'une lettre dans un mot
```python
the_word = "pizza"
the_letter = "z"
if the_letter in the_word:
    print(f"La lettre '{the_letter}' est dans le mot '{the_word}'.")
else:
    print(f"La lettre '{the_letter}' n'est pas dans le mot '{the_word}'.")
```

### Boucle while et affichage d'astérisques
```python
marbles = 5
while marbles > 0:
    print("*" * marbles)
    marbles -= 1
print("You are all out of marbles!")
```

Bonne exploration Python sur IBM Z !
