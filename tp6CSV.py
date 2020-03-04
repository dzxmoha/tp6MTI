import csv

class OpenFile():

    file = open('fichier.csv')
    reader = csv.reader(file)
    data = list(reader)

    for d in data:
        print(d)
    file.close()