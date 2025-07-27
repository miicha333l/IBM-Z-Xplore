# Défi JCL1 : Making Things Happen

## Objectif
Découvrir et manipuler le JCL (Job Control Language) sur IBM Z, comprendre son importance et apprendre à soumettre, analyser et corriger des jobs.

## Prérequis
- Avoir terminé le défi FILES1 (ensembles de données et membres)
- Avoir un profil Zowe Explorer fonctionnel

## Étapes

### 1. Préparation
- Recherchez dans `ZXP.PUBLIC.JCL` le membre `JCLSETUP`.
- Ce job va créer les ensembles de données nécessaires pour ce défi.
- Soumettez ce job sans modification.

### 2. Soumission du job
- Clic droit sur `JCLSETUP` > Submit Job.
- Si vous voyez des erreurs de duplicata, c’est que les ensembles existent déjà (pas grave).

### 3. Filtrer et trouver vos jobs
- Dans la section JOBS de Zowe Explorer, cliquez sur la loupe.
- Propriétaire : votre identifiant Z ; Préfixe : * ; Identité : (laisser vide).
- Recherchez le job `JCLSETUP` soumis.

### 4. Vérification du code de retour
- Ouvrez le job `JCLSETUP` et vérifiez le code de condition (CC).
- CC=0000 : tout est OK. Autre valeur : vérifiez le log pour corriger.

### 5. Copier et soumettre JCL1
- Copiez le membre `JCL1` de `ZXP.PUBLIC.JCL` dans votre propre ensemble de données JCL.
- Soumettez votre copie de `JCL1`.
- Si le job échoue (ex : CC=0012), vérifiez les instructions DD et corrigez-les selon les besoins du programme IEBGENER.
- Consultez la documentation IBM sur IEBGENER si besoin.

### 6. Compiler et exécuter COBOL
- Copiez le membre `JCL2` dans votre ensemble de données JCL.
- Modifiez-le si nécessaire pour que les noms de fichiers DD correspondent au code COBOL.
- Soumettez le job et vérifiez le code de retour.

### 7. Soumettre JCL3
- Ouvrez et soumettez le membre `JCL3`.
- Vérifiez que la sortie contient bien les 10 gares et aucune répétition.
- Si besoin, supprimez l’ensemble de données de sortie avant de resoumettre.

### 8. Validation finale
- Soumettez le job `CHKJCL1` depuis `ZXP.PUBLIC.JCL` pour valider votre travail.
- CC=0000 : défi réussi !
- Si CC=0127, corrigez vos jobs JCL2/JCL3 et recommencez.

## Concepts clés
- **JCL** : Permet de décrire au système les tâches à exécuter (création, copie, compilation, exécution de programmes).
- **JES** : Gère la file d’attente et l’exécution des jobs.
- **DD statement** : Définit les fichiers d’entrée/sortie utilisés par les programmes.
- **DISP** : Contrôle la gestion des ensembles de données (création, suppression, partage).
- **DUMMY** : Utilisé pour indiquer qu’un fichier n’est pas nécessaire pour une étape.

## Astuces
- Consultez les logs (JESMSGLG) pour comprendre les erreurs.
- Les jobs doivent retourner CC=0000 pour être considérés comme réussis.
- Les membres JCL fournis sont à copier dans VOTRE ensemble de données avant modification.
- Les jobs peuvent être soumis plusieurs fois, mais attention aux erreurs de duplicata.

## Exemples de code JCL

### 1. Soumettre un job simple

```jcl
//MONJOB   JOB (ACCT),'EXEMPLE',CLASS=A,MSGCLASS=A,NOTIFY=&SYSUID
//STEP1    EXEC PGM=IEFBR14
```

### 2. Utilisation de DISP

```jcl
//DD1   DD DSN=&SYSUID..MONDATA,DISP=(NEW,CATLG,DELETE),
//         SPACE=(TRK,1),UNIT=SYSDA
```

*Ici, le dataset est créé (NEW), catalogué si succès (CATLG), supprimé si erreur (DELETE).*

### 3. Utilisation de DUMMY

```jcl
//SORTOUT DD DUMMY
```

*Aucune sortie n’est produite, mais la DD est requise par le programme.*

### 4. Instructions DD typiques pour IEBGENER

```jcl
//SYSUT1   DD DSN=&SYSUID..SOURCE,DISP=SHR
//SYSUT2   DD DSN=&SYSUID..CIBLE,DISP=OLD
//SYSPRINT DD SYSOUT=*
//SYSIN    DD DUMMY
```

*SYSUT1 = source, SYSUT2 = cible, SYSPRINT = log, SYSIN = pas de contrôle.*
