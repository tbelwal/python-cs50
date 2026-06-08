import csv

with open("sicilian.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)
