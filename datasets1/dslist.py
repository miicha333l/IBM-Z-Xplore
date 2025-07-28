# dslist.py
# Script pour lister les membres d'un dataset partitionné sur z/OS via ZOAU
# Modifiez la ligne 9 pour pointer vers votre dataset partitionné

import zoautil_py.datasets as datasets

# Remplacez par le nom de votre dataset partitionné
members_list = datasets.list_members('Zxxxxx.JCL')

for member in members_list:
    print(member)
