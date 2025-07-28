# Défi IBM Z Xplore – Datasets et Python

Ce dossier contient les scripts et instructions pour le défi sur les ensembles de données séquentiels et partitionnés, l’utilisation de Python et l’intégration USS.

## Étapes du défi

### 1. Création ou utilisation du dataset séquentiel JCL3OUT
- Si vous avez déjà `JCL3OUT`, utilisez-le. Sinon, créez-en un nouveau via VSCode (clic droit > Créer un nouvel ensemble de données).

### 2. Ajout d’une ligne avec la commande `decho` en USS
```sh
decho a "Cette ligne va en bas" 'Zxxxxx.JCL3OUT'
```
- Remplacez `Zxxxxx` par votre identifiant.
- Connectez-vous en SSH pour exécuter cette commande.

### 3. Extraction et modification du dataset dans VSCode
- Si recréé, faites « Extraire du mainframe » pour avoir la dernière version.
- Vérifiez que la ligne ajoutée apparaît en bas.

### 4. Utilisation de `dslist.py`
- Placez `dslist.py` dans votre répertoire personnel USS.
- Modifiez la ligne 9 pour pointer vers votre dataset partitionné.
- Exécutez avec :
```sh
python3 dslist.py
```

### 5. Correction et exécution de `members.py`
- Ouvrez et complétez `members.py` pour :
  - Créer un dataset séquentiel si besoin.
  - Récupérer la liste de liens via le module `zsystem`.
  - Écrire le résultat dans le dataset séquentiel.
- Utilisez `Zxxxxx.COMPLETE` comme nom de dataset séquentiel.

### 6. Soumission du job CHKAUTO
- Soumettez le job CHKAUTO pour valider le défi.

## Fichiers
- `dslist.py` : script pour lister les membres d’un dataset partitionné.
- `members.py` : script à compléter pour automatiser la gestion des datasets.

## Ressources
- [Documentation ZOAU Python](https://www.ibm.com/docs/en/zoau/1.2.0?topic=referenceclasses)

---
*Challenge IBM Z Xplore – datasets, USS, Python, automation.*
