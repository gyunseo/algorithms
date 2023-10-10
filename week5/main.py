import csv, re


fin = open("data.csv", "r", encoding="utf-8")
csv_fin = csv.reader(fin)
data = []

for i, line in enumerate(csv_fin):
    if i == 0:
        continue
    # get only number
    print(line)
