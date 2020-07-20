from sys import argv
import csv
from cs50 import SQL

if not len(argv) == 2:  # Checking if used correctly, if not printing error
    print("Usage: python import.py <file>.csv")
    exit()

db = SQL("sqlite:///students.db")  # Connecting to students.db

with open(argv[1], "r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")  # Reading CSV file into dictionary
    for row in reader:  # Iterating through said dictionary, creating variables for name, house, birth
        names = row['name']
        names = names.split(" ")
        if len(names) == 2:
            name = [names[0], None, names[1]]
        if len(names) == 3:
            name = [names[0], names[1], names[2]]
        house = row['house']
        birth = row['birth']
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                   name[0], name[1], name[2], house, birth)  # Inserting each student into students.db