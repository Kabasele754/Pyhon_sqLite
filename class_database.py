import sqlite3

class SqLiteForm:
    
    def __init__(self,):
        # ouvert connection 

        self.conn = sqlite3.connect('database.sqlite3')

        #print(f"vous connection a reussi vous creer votre database {conn}")

        # creer un curseur pour permettre a excuter le commande sql
        self.cuseur = self.conn.cursor()
        self.select_all_table()
    
        self.conn.commit()
        
        # fermeture de connecion
        self.conn.close()
        
       
      
        
    def select_all_table(self,):
        
        self.cuseur.execute("""SELECT * FROM etudaiant 
                            
            """)
        print(self.cuseur.fetchall())
        
    
        
          
       
s = SqLiteForm()