# Défi REXX1 – Découverte du langage Rexx et de Zowe CLI

Ce dossier regroupe les instructions et astuces pour le défi REXX1 sur IBM Z Xplore.

## Objectif
Découvrir le langage Rexx, apprendre à exécuter des programmes Rexx en ligne de commande et via TSO avec Zowe CLI.

## Étapes principales
1. **Installer Zowe CLI**
   - Suivre la documentation officielle : [Zowe CLI Install Guide](https://docs.zowe.org/stable/user-guide/cli-installcli/)
   - Vérifier l'installation :
     ```sh
     zowe --version
     ```
2. **Préparer l'environnement**
   - Configurer les profils z/OSMF et TSO dans Zowe CLI.
   - Vérifier la connexion :
     ```sh
     zowe config list
     ```
3. **Copier les programmes Rexx**
   - Copier les membres SOMEREXX et GUESSNUM depuis `ZXP.PUBLIC.SOURCE` vers votre dataset personnel.
4. **Exécuter un programme Rexx**
   - En ligne de commande TSO :
     ```sh
     zowe tso issue command "exec 'Zxxxxx.SOURCE(somerexx)'" --ssm
     ```
   - Remplacez `Zxxxxx` par votre identifiant Z.
5. **Démarrer un espace d'adressage TSO**
   - Créer un espace d'adressage :
     ```sh
     zowe tso start as
     ```
   - Utiliser la clé retournée pour envoyer des commandes interactives.
6. **Jouer avec GUESSNUM**
   - Exécuter le programme GUESSNUM dans l'espace d'adressage TSO.
   - Interagir avec le programme en envoyant des données via Zowe CLI.

## Ressources utiles
- [Documentation Rexx](https://www.ibm.com/docs/en/zos/2.4.0?topic=languages-rexx)
- [Zowe CLI](https://docs.zowe.org/stable/)


## Exemples de code Rexx

### Exemple 1 : Afficher un message
```rexx
/* Un simple programme Rexx */
say "Hello, IBM Z Xplore!"
```

### Exemple 2 : Boucle et calcul
```rexx
/* Compter de 1 à 5 et afficher la somme */
sum = 0
do i = 1 to 5
  say "Valeur :" i
  sum = sum + i
end
say "Somme totale :" sum
```

### Exemple 3 : Lecture d'une entrée utilisateur
```rexx
/* Demander un nombre et afficher s'il est pair ou impair */
say "Entrez un nombre :"
pull n
if n // 2 = 0 then
  say n ", c'est un nombre pair."
else
  say n ", c'est un nombre impair."
```

Bonne découverte du langage Rexx et de Zowe CLI sur IBM Z !
