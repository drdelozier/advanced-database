import sqlite3

connection = sqlite3.connect("pets.db")

cursor = connection.cursor()

rows = cursor.execute("select name, kind from pet, species where species_id = species.id")
rows = list(rows)
print(rows)
for row in rows:
    name, kind = row
    print(name)
    print(kind)
    print(f"my {kind} was named {name}.")

print("done.")