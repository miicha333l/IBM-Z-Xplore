# members.py
# Script pour créer un dataset séquentiel, récupérer la liste de liens, et écrire le résultat
# Complétez les parties indiquées pour le défi IBM Z Xplore

import zoautil_py.datasets as datasets
import zoautil_py.jobs as jobs
import zoautil_py.zsystem as zsystem
import sys

# Demande le nom du dataset séquentiel
print("Entrez le nom de l'ensemble de données séquentiel :")
dsname = input().strip()

# Vérifie si le dataset existe
if not datasets.exists(dsname):
    print(f"Le dataset {dsname} n'existe pas. Voulez-vous le créer ? (o/n)")
    if input().lower() == 'o':
        # Création du dataset séquentiel
        datasets.create(dsname, "SEQ")
    else:
        print("Arrêt du programme.")
        sys.exit()

# Récupère la liste de liens

# Récupère la liste de liens
linklist_output = zsystem.linklist()

# Écrit la liste de liens dans le dataset séquentiel

# Écrit la liste de liens dans le dataset séquentiel
datasets.write(dsname, linklist_output)

print(f"La liste de liens a été écrite dans {dsname}.")
