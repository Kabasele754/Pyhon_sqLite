

SQLite est une bibliothèque écrite en langage C qui propose un moteur de base de données relationnelle accessible par le langage SQL. SQLite implémente en grande partie le standard SQL-92 et des propriétés ACID.

Contrairement aux serveurs de bases de données traditionnels, comme MySQL ou PostgreSQL, sa particularité est de ne pas reproduire le schéma habituel client-serveur mais d'être directement intégrée aux programmes. L'intégralité de la base de données (déclarations, tables, index et données) est stockée dans un fichier indépendant de la plateforme.

D. Richard Hipp, le créateur de SQLite, a choisi de mettre cette bibliothèque ainsi que son code source dans le domaine public, ce qui permet son utilisation sans restriction aussi bien dans les projets open source que dans les projets propriétaires. Le créateur ainsi qu'une partie des développeurs principaux de SQLite sont employés par la société américaine Hwaci2.

SQLite est le moteur de base de données le plus utilisé au monde, grâce à son utilisation :

dans de nombreux logiciels grand public comme Firefox, Skype, Google Gears,

dans certains produits d'Apple, d'Adobe et de McAfee,

dans les bibliothèques standards de nombreux langages comme PHP ou Python.

De par son extrême légèreté (moins de 600 Kio3), il est également très populaire sur les systèmes embarqués, notamment sur la plupart des smartphones et tablettes modernes : les systèmes d'exploitation mobiles iOS, Android et Symbian l'utilisent comme base de données embarquée4. Au total, on peut dénombrer plus d'un milliard de copies connues et déclarées de la bibliothèque5.


# crud
## 1. create

```sql
CREATE TABLE student (
	id_s	INTEGER,
	name	varchar(10), 
	lastname	varchar(15),
	email	varchar(20),
	phone1 varchar(20),
	PRIMARY KEY("id_s" AUTOINCREMENT)
)


CREATE TABLE course (
	id_c	INTEGER,
	title	varchar(20), 
	edition	varchar(15),
	author	varchar(20),
	id_etr	INTEGER,
	PRIMARY KEY("id_c" AUTOINCREMENT),
	FOREIGN KEY(id_etr) REFERENCES student(id_s)
)
```
## 1.1 insert

```sql
INSERT INTO student(id_s,name,lastname,email,phone1)
VALUES(1,"ilunga","kazadi","ilunga@gmail.com","0999988334");

INSERT INTO student(id_s,name,lastname,email,phone1)
VALUES(2,"ngoie","kasongo","ngoier@gmail.com","0999956734");

INSERT INTO student 
VALUES(3,"mwamba","mwamba","mwamba@gmail.com","0999956734");
```
``` sql
INSERT INTO course(id_c,title,edition,author,id_etr)
VALUES(1,"algorithme","5eme","genie of genie",1);

INSERT INTO course(id_c,title,edition,author,id_etr)
VALUES(2,"python","5eme","Acen",2);

INSERT INTO course 
VALUES(3,"java","20 eme","hergy",3);

INSERT INTO course 
VALUES(4,"html avancee","34 eme","josh",2);

INSERT INTO course 
VALUES(5,"uml 3","30 eme","josh",1);

INSERT INTO course 
VALUES(6,"boostrapp","30 eme","josh",3);
```
## 2 Select or read
``` sql
SELECT * FROM student WHERE id_s = 1 or id_s = 2 ;
SELECT * FROM student;
SELECT name, email FROM student;
SELECT phone1 FROM student;
```
``` sql
SELECT * FROM course;

SELECT * FROM course WHERE id_etr = 1;

SELECT * FROM course WHERE id_etr = 2;

SELECT * FROM course WHERE title = 'java';

SELECT * FROM course WHERE author = 'josh';
```

## 4 Update 
```sql
UPDATE student SET name= "mutemba", email="mutemba@gmail.com" WHERE id_s = 3
UPDATE course SET id_etr=1  WHERE id_c = 4

```

