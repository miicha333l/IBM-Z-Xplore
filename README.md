# IBM Z Xplore - Défis fondamentaux

Ce dépôt regroupe les solutions et explications des principaux défis techniques réalisés sur la plateforme IBM Z Xplore.

## Structure des dossiers

- [`📦 vsc1/`](./vsc1) — VS Code, Zowe Explorer  
  Connectez-vous au mainframe IBM Z via VS Code et Zowe Explorer.
- [`🗂️ jcl1/`](./jcl1) — JCL, IBM Z  
  Making Things Happen : soumission de jobs et concepts JCL.
- [`📝 files1/`](./files1) — Datasets, IBM Z  
  How Data Gets Down on z/OS : gestion des ensembles de données et membres.
- [`💻 uss1/`](./uss1) — UNIX System Services, Shell  
  Découverte de l’environnement UNIX sur z/OS, navigation et scripts.
- [`🐍 code1/`](./code1) — Python  
  Premiers pas en Python sur IBM Z.
- [`🧩 rexx1/`](./rexx1) — Rexx, Zowe CLI  
  Découverte du langage Rexx et de Zowe CLI.
- [📁 datasets1](./datasets1) — Datasets séquentiels, partitionnés et automatisation Python

Chaque dossier contient un fichier README.md spécifique au défi, avec instructions, astuces et exemples de code pour réussir l’exercice.

---

N’hésitez pas à explorer chaque dossier pour progresser dans votre apprentissage IBM Z !

---

## 🚀 Défis avancés

Vous venez d’atteindre le niveau avancé sur IBM Z Xplore !  
Cette rubrique regroupe les solutions, explications et ressources pour les défis avancés, notamment :

- JCL et automatisation avancés
- Sécurité et RACF
- Programmation système
- Optimisation des performances
- Datasets et utilitaires avancés
- Intégration du mainframe avec des outils modernes


### [`� cobol1/`](./cobol1) — COBOL, IBM Z
Défi COBOL « ADDAMT » : programme qui lit un numéro de client et trois montants, puis affiche le total.

**Fichiers principaux :**
- `ADDAMT.cbl` : Code source COBOL du défi.

**Instructions :**
1. Transférez le fichier `ADDAMT.cbl` sur votre mainframe IBM Z.
2. Compilez le programme COBOL via JCL ou Zowe CLI.
3. Soumettez le job JCL associé pour exécuter le programme.
4. Vérifiez la sortie dans le spool ou via Zowe CLI.

Exemple de soumission avec Zowe :
```sh
zowe zos-jobs submit data-set "VOTRE.DATASET.JCL(MEMBREJCL)" --wait-for-output --response-format-json
```

**Astuces :**
- Adaptez le JCL selon votre environnement (nom de dataset, paramètres…).
- Consultez le README principal pour plus de ressources sur IBM Z Xplore.

---

Explorez cette section pour des astuces, exemples de code et guides afin de maîtriser les sujets avancés sur IBM Z.
