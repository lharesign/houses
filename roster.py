from sys import argv
import csv
from cs50 import SQL

if not len(argv) == 2:  # Checking if used correctly, if not printing error
    print("Usage: python roster.py <house name>")
    exit()

db = SQL("sqlite:///students.db")

house = argv[1]
print(house)

# Fetching the students for each house and storing in variable
roster = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first", house)

for row in roster:  # Iterating through roster variable (dict) and printing out necessary info
    if row['middle'] != None:
        print(f"{row['first']} {row['middle']} {row['last']}, born {row['birth']}")
    else:
        print(f"{row['first']} {row['last']}, born {row['birth']}")

