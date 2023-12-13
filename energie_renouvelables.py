import csv
import matplotlib.pyplot as plt

table = []

with open('RTE_2020.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    entetes = next(csv_reader)  # Lire la première ligne comme entêtes
    for ligne in csv_reader:
        table.append(dict(zip(entetes, ligne)))

table_vide = []
for ligne in table:
    if all(ligne.values()):
        table_vide.append(ligne)

#Calculer la consommation totale
total_consommation = sum(int(ligne['Consommation']) for ligne in table_vide)

energie = ['Fioul', 'Charbon', 'Gaz',
           'Nucleaire', 'Eolien', 'Solaire',
           'Hydraulique', 'Bioenergies']

energie_total = [sum(int(ligne[source]) for ligne in table_vide) for source in energie]

plt.figure(figsize=(8, 8))
plt.pie(energie_total, labels=energie, autopct='%1.1f%%')
plt.title('Énergies Renouvelables dans la Production en France en 2020')
plt.show()

print(f'Consommation Totale en 2020 : {total_consommation}')
