# Défi COBOL « ADDAMT »

Ce dossier contient le programme COBOL `ADDAMT.cbl` réalisé dans le cadre du défi IBM Z Xplore.

## Description

Ce programme lit un numéro de client et trois montants, puis affiche le total.

## Fichiers

- `ADDAMT.cbl` : Code source COBOL du défi.

## Instructions pour exécuter le programme

1. Transférez le fichier `ADDAMT.cbl` sur votre mainframe IBM Z.
2. Compilez le programme COBOL via JCL ou Zowe CLI.
3. Soumettez le job JCL associé pour exécuter le programme.
4. Vérifiez la sortie dans le spool ou via Zowe CLI.

Exemple de soumission avec Zowe :
```sh
zowe zos-jobs submit data-set "VOTRE.DATASET.JCL(MEMBREJCL)" --wait-for-output --response-format-json
```

## Astuces

- Adaptez le JCL selon votre environnement (nom de dataset, paramètres…).
- Consultez le README principal pour plus de ressources sur IBM Z Xplore.
