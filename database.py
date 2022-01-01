import sqlite3

# ouvert connection 

conn = sqlite3.connect('database.sqlite3')

#print(f"vous connection a reussi vous creer votre database {conn}")

# creer un curseur pour permettre a excuter le commande sql
cuseur = conn.cursor()

# Creer la methode excute

cuseur.execute(
    """INSERT INTO cours 
        VALUES(
        4,
        "JavaScript",
        90
        
    );""")

print("votre insertion a reussi")

conn.commit()


# fermeture de connecion
conn.close()