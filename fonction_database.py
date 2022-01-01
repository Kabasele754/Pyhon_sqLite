import sqlite3


# Fonction pour ajouter dans la table
def table():
    con_db = sqlite3.connect('database.sqlite3')
    c = con_db.cursor()
    try:
        #c.execute("PRAGMA foreign_key = on ")
        c.executescript("""CREATE TABLE etudiant(
            id_enseignant INTEGER PRIMARY KEY  AUTOINCREMENT UNIQUE,  nom TEXT,postnom TEXT,age INT);
            
            CREATE TABLE etudiant(
            id_etudiant INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,  nom TEXT,postnom TEXT,age INT);
            
            CREATE TABLE fiche(
            nom TEXT,desc TEXT,nume_fich INT,   id_en INTEGER,  id_et INTEGER, FOREIGN KEY(id_en) REFERENCES enseignants( id_enseignant), FOREIGN KEY(id_et) REFERENCES etudiant(id_etudiant));
            
            """)
        
        print(f"Vous avez creer les tables ")
        
    except sqlite3.IntegrityError:
        print(f"Cette clef existe : <{id}> deja ")
    con_db.commit()
    con_db.close()
    

# Fonction pour ajouter dans la base de donne
def add(list):
    # add(id,nom,postnom,age) 1
    con_db = sqlite3.connect('database.sqlite3')
    c = con_db.cursor()
    try:
        '''
         c.executemany("""INSERT INTO enseignants VALUES(
            ?,?,?,?)""",id,nom,postnom,age) # 1
        '''
        c.executemany("""INSERT INTO enseignants VALUES(
            ?,?,?,?)""",list)
        for i in list:
        
            print(f"Vous ajoutez le cours numero {i[1]} son titre {i[2]} et son credit est {i[3]}")
        
    except sqlite3.IntegrityError:
        print(f"Cette clef existe : <{list[0]}> deja ")
    con_db.commit()
    con_db.close()
    
# La fonction pour la supprission d'information    
def delete(id=0):
    con_db = sqlite3.connect('database.sqlite3')
    c = con_db.cursor()
    
    try:
        if str(id) != str(c.execute("""DELETE FROM cours WHERE id_cours = (?) """,(id))):
           print(f"la clef {id} n'existe pas ")
           
        else:
            print(f"Vous avez supprimer {id}")
            
    except ValueError:
        print("Vous devez mettre vos valeur en numerique entre '' comme par exemple '1' '2' '3', '45' ect...")
    
    except sqlite3.IntegrityError:
        print(f"Cette <{id}> clef n'existe pas ")
    
  
    con_db.commit()
    con_db.close()
    

# La fonction pour la Mise à jour d'information    
def update(id,titre,credit):
    con_db = sqlite3.connect('database.sqlite3')
    c = con_db.cursor()
    
    try:
      if id != c.execute("""UPDATE cours set titre= (?), credit = (?) WHERE id_cours = (?) """,(titre, credit, id)):
        print(f"Votre clef {id} n'existe pas ")
        c.execute("""INSERT INTO cours VALUES(
            ?,?,?)""",(id,titre,credit))
        print(f"Vous ajoutez le cours numero {id} son titre {titre} et son credit est {credit}")

            
    except ValueError:
        print("Vous devez mettre vos valeur en numerique entre '' comme par exemple '1' '2' '3', '45' ect...")
    
    except sqlite3.IntegrityError:
        print(f"Cette <-{id}-> clef existe pas ")
        print(f"Votre mise à jour du cour de {titre} et son {credit}")
    
  
    con_db.commit()
    con_db.close()
    

#update(14,"Python",69)
#table()
"""
list_etudiant = [
    (221,"Achille", "Achille", 12),
    (223,"franck","franck",11),
    (224,"deborah","deborah",10),
    (225,"Jovial","jovial",2),
    (226,"Josmar","Josmar",1),
    (227,"Gedeon","gedeon",4),
    (228,"chancelle","chancelle",3),
    (226,"marie","marie",13),
]

for i in list_etudiant:
    
    add(i[0],i[1],i[2],i[3])
    
"""


list_enseignat = [
    (1,"Achille", "Achille", 12),
    (2,"franck","franck",11),
    (3,"deborah","deborah",10),
    (4,"Jovial","jovial",2),
    (5,"Josmar","Josmar",1),
    (6,"Gedeon","gedeon",4),
    (7,"chancelle","chancelle",3),
    (8,"marie","marie",13),
]

add(list_enseignat)

