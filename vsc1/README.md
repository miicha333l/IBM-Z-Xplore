
# Défi VSC1 : Connectez-vous

## Objectif

Se connecter au serveur IBM Z via le plugin Zowe Explorer pour VS Code. Ce défi vous guide dans l’installation des outils nécessaires et la configuration de votre première connexion mainframe.

## Prérequis

- Identifiant et mot de passe IBM Z fournis par la plateforme
- Connexion internet
- Environ 45 minutes

## Étapes

### 1. Vérification de la connexion au serveur

- Accédez à : [https://204.90.115.200:10443/zosmf/info](https://204.90.115.200:10443/zosmf/info)
- Si la page IBM Z Xplore s’affiche, continuez. Sinon, vérifiez votre réseau ou contactez votre fournisseur.

### 2. Téléchargements nécessaires

- [Node.js (version LTS)](https://nodejs.org/fr/)
- [Java Runtime (LTS recommandé)](https://developer.ibm.com/languages/java/semeruruntimes/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/download)

### 3. Installation

- Installez Node.js, Java et VS Code selon votre système d’exploitation.
- Lancez VS Code.

### 4. Installation des extensions VS Code

- Ouvrez le gestionnaire d’extensions (icône de 4 carrés à gauche).
- Recherchez et installez : **IBM Z Open Editor** (inclut Zowe Explorer).

### 5. Découverte de Zowe Explorer

- Une nouvelle icône Zowe apparaît dans la barre latérale.
- Cliquez dessus pour ouvrir Zowe Explorer.

### 6. Création du profil de connexion

- Cliquez sur le + à côté de « ENSEMBLES DE DONNÉES ».
- Sélectionnez « Créer un fichier de configuration d’équipe » (ou modifiez le profil existant).
- Choisissez l’emplacement Global.
- Dans le fichier `zowe.config.json` :
  - Section `zosmf` : port = 10443
  - Section `tso` : compte = FB3
  - Section de base :
    - host = 204.90.115.200
    - rejectUnauthorized = false
- Enregistrez le fichier.

### 7. Ajout de vos identifiants

- Clic droit sur la connexion créée > Gérer le profil > Mettre à jour les informations d’identification.
- Saisissez votre identifiant Z et votre mot de passe Z.

### 8. Vérification de la connexion

- Passez la souris sur la connexion > cliquez sur la loupe > entrez votre identifiant Z (ex : Z12345).
- Vérifiez l’accès à vos jeux de données.

### 9. Résolution des problèmes

- En cas d’erreur, mettez à jour ou supprimez le profil, puis redémarrez VS Code si besoin.

### 10. Validation du défi

- Naviguez dans ENSEMBLES DE DONNÉES > ZXP.PUBLIC.JCL > CHKVSC.
- Faites un clic droit sur CHKVSC > « Soumettre le travail ».
- Vérifiez la complétion du défi sur la plateforme IBM Z Xplore.

## Astuces

- Votre identifiant Z est personnel (ex : Z12345).
- Les mots de passe expirent tous les 60 jours.
- Explorez les autres sections (USS, Jobs) pour la suite des défis.

- Installez Node.js, Java et VS Code selon votre système d’exploitation.
- Lancez VS Code.

### 4. Installation des extensions VS Code

- Ouvrez le gestionnaire d’extensions (icône de 4 carrés à gauche).
- Recherchez et installez : **IBM Z Open Editor** (inclut Zowe Explorer).

### 5. Découverte de Zowe Explorer

- Une nouvelle icône Zowe apparaît dans la barre latérale.
- Cliquez dessus pour ouvrir Zowe Explorer.

### 6. Création du profil de connexion

- Cliquez sur le + à côté de « ENSEMBLES DE DONNÉES ».
- Sélectionnez « Créer un fichier de configuration d’équipe » (ou modifiez le profil existant).
- Choisissez l’emplacement Global.
- Dans le fichier `zowe.config.json` :
  - Section `zosmf` : port = 10443
  - Section `tso` : compte = FB3
  - Section de base :
    - host = 204.90.115.200
    - rejectUnauthorized = false
- Enregistrez le fichier.

### 7. Ajout de vos identifiants

- Clic droit sur la connexion créée > Gérer le profil > Mettre à jour les informations d’identification.
- Saisissez votre identifiant Z et votre mot de passe Z.

### 8. Vérification de la connexion

- Passez la souris sur la connexion > cliquez sur la loupe > entrez votre identifiant Z (ex : Z12345).
- Vérifiez l’accès à vos jeux de données.

### 9. Résolution des problèmes

- En cas d’erreur, mettez à jour ou supprimez le profil, puis redémarrez VS Code si besoin.

### 10. Validation du défi

- Naviguez dans ENSEMBLES DE DONNÉES > ZXP.PUBLIC.JCL > CHKVSC.
- Faites un clic droit sur CHKVSC > « Soumettre le travail ».
- Vérifiez la complétion du défi sur la plateforme IBM Z Xplore.

## Astuces

- Votre identifiant Z est personnel (ex : Z12345).
- Les mots de passe expirent tous les 60 jours.
- Explorez les autres sections (USS, Jobs) pour la suite des défis.
