import sqlite3

# DB-API spec for talking to relational databases in Python

connection = sqlite3.connect("pets.db")

cursor = connection.cursor()

cursor.execute("drop table pet")
cursor.execute("drop table species")

cursor.execute("create table pet (id integer primary key, name text, species_id int)")

cursor.execute("create table species (id integer primary key, kind text)")

cursor.execute("insert into species (kind) values ('dog')")
cursor.execute("insert into species (kind) values ('cat')")
cursor.execute("insert into species (kind) values ('fish')")

cursor.execute("insert into pet (name, species_id) values ('dorothy',1)")
cursor.execute("insert into pet (name, species_id) values ('muffin',2)")
cursor.execute("insert into pet (name, species_id) values ('suzy',1)")
cursor.execute("insert into pet (name, species_id) values ('angel',3)")

connection.commit()
connection.close()

print("done.")

