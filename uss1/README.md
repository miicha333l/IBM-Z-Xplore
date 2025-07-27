# Défi USS1 : CD CIRCLE && CD .. && CD && ./SHAKE_IT_ALL_ABOUT.SH

## Objectif
Découvrir UNIX System Services (USS) sur z/OS, apprendre à naviguer, manipuler des fichiers et répertoires, exécuter des scripts shell, et utiliser la redirection de sortie.

## Prérequis
- Avoir accès au système IBM Z et à VSCode
- Avoir terminé le défi VSC1

## Étapes principales

### 1. Ouvrir le terminal
- Ouvre la section Terminal dans VSCode (menu Terminal > Nouveau terminal).
- Si besoin, utilise un client SSH (ex : PuTTY) sur Windows.

### 2. Connexion SSH
- Commande :
  ```sh
  ssh zxxxxx@204.90.115.200
  ```
  (remplace zxxxxx par ton identifiant)
- Accepte les messages de sécurité et entre ton mot de passe (rien ne s’affiche, c’est normal).

### 3. Découverte de l’environnement
- Utilise `ls` pour lister les fichiers/répertoires.
- Si ton répertoire est vide, exécute `usssetup` puis `ls`.
- Utilise `exit` pour te déconnecter.

### 4. Navigation
- `pwd` : affiche le chemin courant
- `cd nom_repertoire` : change de dossier
- `cd ..` : remonte d’un niveau
- `cd ~` : retourne au dossier personnel
- `cd /z/public/test` : va directement à un chemin absolu
- Utilise la touche Tab pour l’auto-complétion et les flèches haut/bas pour rappeler/modifier des commandes.

### 5. Créer fichiers et dossiers
- `touch monfichier` : crée un fichier vide
- `mkdir mondossier` : crée un dossier
- `ls` pour vérifier

### 6. Voir USS dans Zowe
- Dans la vue USS de Zowe Explorer, filtre sur `/z/zxxxxx` (remplace par ton identifiant, en minuscules).

### 7. Exécuter un script
- Vérifie les droits avec `ls -l` (le fichier doit avoir un `x` pour être exécutable).
- Exécute :
  ```sh
  ./scramble.sh
  ```
- Trouve la bonne valeur de rotation (entre 1 et 26) pour décoder le message.

### 8. Supprimer et restaurer
- `rm monfichier` : supprime un fichier
- `rmdir mondossier` : supprime un dossier vide
- Pour restaurer un fichier perdu :
  ```sh
  cp /z/public/test ~/test
  ```

### 9. Redirection de sortie
- Pour enregistrer la sortie dans un fichier :
  ```sh
  ./scramble.sh > ussout.txt
  ```
- Pour ajouter la sortie d’une commande à la fin du fichier :
  ```sh
  du -ak >> ussout.txt
  date >> ussout.txt
  ```
- Vérifie le contenu avec :
  ```sh
  cat ussout.txt
  ```

### 10. Validation
- Soumets le job `CHKUSS1` dans `ZXP.PUBLIC.JCL` pour valider.
- CC=0000 : défi réussi !

## Commandes utiles
- `ls`, `pwd`, `cd`, `touch`, `mkdir`, `rm`, `rmdir`, `cp`, `cat`, `du`, `date`, `exit`
- Redirection : `>`, `>>`

## Astuces
- Utilise Tab pour l’auto-complétion.
- Utilise les flèches haut/bas pour rappeler/modifier des commandes.
- Rafraîchis la vue USS dans VSCode après modification.
