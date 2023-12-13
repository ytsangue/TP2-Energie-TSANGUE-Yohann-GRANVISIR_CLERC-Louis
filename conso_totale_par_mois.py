#importation du fichier
import csv
conso_totale=[]
with open('RTE_2020.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        conso_totale.append(row)

#suppression de la premiere et derniere ligne
del conso_totale[0]
del conso_totale[len(conso_totale)-1]

#suppression des lignes vides en supprimant les lignes paires et 
#en creeant une nouvelle liste de listes
conso_totale1 = [liste for index, liste in enumerate(conso_totale) if index % 2 == 0]

#calcul la consommation totale par mois en utilisant des expressions regulieres
#sur la case date pour separer par mois
import re
janvier = 0
fevrier = 0
mars = 0
avril = 0
mai = 0
juin = 0
juillet = 0
aout = 0
septembre = 0
octobre = 0
novembre = 0
decembre = 0
for element in conso_totale1:
    if re.fullmatch("2020-01-\d+", element[2]):
        janvier = janvier + int(element[4])
    elif re.fullmatch("2020-02-\d+", element[2]):
        fevrier = fevrier + int(element[4])
    elif re.fullmatch("2020-03-\d+", element[2]):
        mars = mars + int(element[4])
    elif re.fullmatch("2020-04-\d+", element[2]):
        avril = avril + int(element[4])
    elif re.fullmatch("2020-05-\d+", element[2]):
        mai = mai + int(element[4])
    elif re.fullmatch("2020-06-\d+", element[2]):
        juin = juin + int(element[4])
    elif re.fullmatch("2020-07-\d+", element[2]):
        juillet = juillet + int(element[4])
    elif re.fullmatch("2020-08-\d+", element[2]):
        aout = aout + int(element[4])
    elif re.fullmatch("2020-09-\d+", element[2]):
        septembre = septembre + int(element[4])
    elif re.fullmatch("2020-10-\d+", element[2]):
        octobre = octobre + int(element[4])
    elif re.fullmatch("2020-11-\d+", element[2]):
        novembre = novembre + int(element[4])
    elif re.fullmatch("2020-12-\d+", element[2]):
        decembre = decembre + int(element[4])

#pareil mais avec les previsions
prev_janvier = 0
prev_fevrier = 0
prev_mars = 0
prev_avril = 0
prev_mai = 0
prev_juin = 0
prev_juillet = 0
prev_aout = 0
prev_septembre = 0
prev_octobre = 0
prev_novembre = 0
prev_decembre = 0
for element in conso_totale1:
    if re.fullmatch("2020-01-\d+", element[2]):
        prev_janvier = prev_janvier + int(element[6])
    elif re.fullmatch("2020-02-\d+", element[2]):
        prev_fevrier = prev_fevrier + int(element[6])
    elif re.fullmatch("2020-03-\d+", element[2]):
        prev_mars = prev_mars + int(element[6])
    elif re.fullmatch("2020-04-\d+", element[2]):
        prev_avril = prev_avril + int(element[6])
    elif re.fullmatch("2020-05-\d+", element[2]):
        prev_mai = prev_mai + int(element[6])
    elif re.fullmatch("2020-06-\d+", element[2]):
        prev_juin = prev_juin + int(element[6])
    elif re.fullmatch("2020-07-\d+", element[2]):
        prev_juillet = prev_juillet + int(element[6])
    elif re.fullmatch("2020-08-\d+", element[2]):
        prev_aout = prev_aout + int(element[6])
    elif re.fullmatch("2020-09-\d+", element[2]):
        prev_septembre = prev_septembre + int(element[6])
    elif re.fullmatch("2020-10-\d+", element[2]):
        prev_octobre = prev_octobre + int(element[6])
    elif re.fullmatch("2020-11-\d+", element[2]):
        prev_novembre = prev_novembre + int(element[6])
    elif re.fullmatch("2020-12-\d+", element[2]):
        prev_decembre = prev_decembre + int(element[6])

#affchage des resultats sous forme de diagramme en barres
import matplotlib.pyplot as plt
largeur_barre = 0.3
y1 = [janvier,fevrier,mars,avril,mai,juin,juillet,aout,septembre,octobre,novembre,decembre]
y2 = [prev_janvier,prev_fevrier,prev_mars,prev_avril,prev_mai,prev_juin,prev_juillet,prev_aout,prev_septembre,prev_octobre,prev_novembre,prev_decembre]
x1 = range(len(y1))
x2 = [i + largeur_barre for i in x1]
plt.bar(x1,y1, width = largeur_barre, color = 'blue', linewidth = 2)
plt.bar(x2,y2, width = largeur_barre, color = 'orange', linewidth = 2)
plt.xticks([r + largeur_barre / 2 for r in range(len(y1))],['janvier','fevrier','mars','avril','mai','juin','juillet','aout','septembre','octobre','novembre','decembre'])
plt.title("Consommation totale d'énergie par mois (bleu) en 2020 et comparaison avec les prévisions (orange)")
plt.show()