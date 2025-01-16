import csv

csv_filename = 'OlympicMedals_2020.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    headers = csv_file.readline()
    reader = csv.reader(csv_file)
    for i in reader:
        i = [int(j) if j.isnumeric() else j for j in i]
        print(i)
