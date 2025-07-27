# Défi FILES1 : How Data Gets Down on z/OS

## Objectif
Découvrir la gestion des ensembles de données et des membres sur z/OS, apprendre à filtrer, copier, renommer, supprimer et créer des membres, et comprendre la différence entre ensembles de données partitionnés (PDS) et séquentiels.

## Prérequis
- Avoir accès au système IBM Z et avoir configuré VSCode
- Avoir terminé le défi VSC1

## Étapes principales

### 1. Affiner le filtre
- Cliquez sur la loupe à droite de votre profil Zowe Explorer.
- Entrez : `Zxxxxx, ZXP.PUBLIC` (remplacez Zxxxxx par votre identifiant Z).
- Enregistrez le filtre pour voir vos ensembles de données et ceux en lecture seule.

### 2. Accès en lecture seule
- Les ensembles de données ZXP.PUBLIC sont en lecture seule : vous pouvez les copier mais pas les modifier.
- Modifiez uniquement vos propres ensembles de données Zxxxxx.

### 3. Création automatique des datasets
- Ouvrez `ZXP.PUBLIC.JCL` et soumettez le membre `PDSBUILD` (clic droit > Submit Job).
- Cela crée tous les ensembles de données nécessaires pour ce défi.

### 4. Explorer vos datasets
- Rafraîchissez la vue "DATA SETS".
- Repérez votre dataset partitionné `Zxxxxx.INPUT` et explorez ses membres.

### 5. Recommencer si besoin
- Si besoin, resoumettez `PDSBUILD` pour réinitialiser vos datasets.

### 6. Renommer un membre
- Trouvez le membre à renommer dans `INPUT`, clic droit > Rename Member, entrez le nouveau nom.

### 7. Supprimer un membre
- Trouvez le membre à supprimer dans `INPUT`, clic droit > Delete Member, confirmez.

### 8. Copier un membre
- Ouvrez le dataset `SURPRISE`, copiez le membre demandé (clic droit > Copy).

### 9. Coller un membre
- Dans `INPUT`, clic droit > Paste Member, donnez-lui le même nom qu’à l’origine.

### 10. Accès séquentiel
- Ouvrez votre dataset `SEQDS` (séquentiel), ajoutez une ligne de texte et sauvegardez.

### 11. Créer un nouveau membre
- Dans `INPUT`, clic droit > Create New Member, nommez-le `MYNEWMBR`.

### 12. Vérification finale
- Votre dataset `INPUT` doit contenir 5 membres (2 d’origine, 1 renommé, 1 créé, 1 copié), sans le membre supprimé.
- `SEQDS` doit contenir une ligne supplémentaire.
- Soumettez le job `CHKFILES` dans `ZXP.PUBLIC.JCL` pour valider.
- CC=0000 : défi réussi !

## Concepts clés
- **PDS (Partitioned Data Set)** : ensemble de données contenant plusieurs membres (fichiers internes).
- **Séquentiel** : ensemble de données simple, chaque ligne est un enregistrement.
- **Lecture seule** : ZXP.PUBLIC ne peut pas être modifié, seulement copié.
- **Actions courantes** : Renommer, supprimer, copier, coller, créer des membres.

## Astuces
- Rafraîchissez la vue si un membre n’apparaît pas.
- Les noms de membres doivent faire 1 à 8 caractères (A-Z, 0-9, @, #, $).
- Si une étape échoue, recommencez ou vérifiez les instructions.

## Exemples de code JCL

### Créer un dataset partitionné (PDS)

```jcl
//CREPDS   JOB (ACCT),'CREER PDS',CLASS=A,MSGCLASS=A,NOTIFY=&SYSUID
//STEP1    EXEC PGM=IEFBR14
//PDS      DD DSN=&SYSUID..MONPDS,DISP=(NEW,CATLG,DELETE),
//            SPACE=(CYL,1,1,10),UNIT=SYSDA,DSORG=PO
```

### Créer un dataset séquentiel

```jcl
//CRESEQ   JOB (ACCT),'CREER SEQ',CLASS=A,MSGCLASS=A,NOTIFY=&SYSUID
//STEP1    EXEC PGM=IEFBR14
//SEQ      DD DSN=&SYSUID..MONSEQ,DISP=(NEW,CATLG,DELETE),
//            SPACE=(TRK,1),UNIT=SYSDA,DSORG=PS
```

### Copier un membre d'un PDS à un autre

```jcl
//COPYMBR  JOB (ACCT),'COPIER MEMBRE',CLASS=A,MSGCLASS=A,NOTIFY=&SYSUID
//STEP1    EXEC PGM=IEBCOPY
//SYSPRINT DD SYSOUT=*
//SYSUT1   DD DSN=&SYSUID..SOURCEPDS,DISP=SHR
//SYSUT2   DD DSN=&SYSUID..DESTPDS,DISP=SHR
//SYSIN    DD *
  COPY INDD=SYSUT1,OUTDD=SYSUT2
  SELECT MEMBER=MONMBR
/*
```

### Supprimer un membre d'un PDS

```jcl
//DELMEMB  JOB (ACCT),'SUPPRIMER MEMBRE',CLASS=A,MSGCLASS=A,NOTIFY=&SYSUID
//STEP1    EXEC PGM=IEHPROGM
//SYSPRINT DD SYSOUT=*
//DD1      DD DSN=&SYSUID..MONPDS,DISP=SHR
//SYSIN    DD *
  DELETE 'MONPDS(MONMBR)' MEMBER
/*
```

---
Bravo pour avoir terminé ce défi sur la gestion des données sur z/OS !
