
SQLite est le moteur de base de données le plus utilisé au monde, grâce à son utilisation :

dans de nombreux logiciels grand public comme Firefox, Skype, Google Gears,

dans certains produits d'Apple, d'Adobe et de McAfee,

dans les bibliothèques standards de nombreux langages comme PHP ou Python.

# comment installer le logiciel DB browsersqlite3

## Windows
Notre dernière version (3.12.2) pour Windows :

- Navigateur DB pour SQLite - Programme d'installation standard pour [Windows 32 bits](https://download.sqlitebrowser.org/DB.for.SQLite-3.12-win32.msi)
- Navigateur DB pour SQLite - .zip (pas d'installateur) pour [Windows 32 bits](https://download.sqlitebrowser.org/DB.for.SQLite-3.12-win32.zip)

- Navigateur DB pour SQLite - Programme d'installation standard pour [Windows 64 bits](https://download.sqlitebrowser.org/DB.for.SQLite-3.12-win64.msi)
- Navigateur DB pour SQLite - .zip (pas d'installateur) pour [Windows 64 bits](https://download.sqlitebrowser.org/DB.for.SQLite-3.12-win64.zip)

Remarque - Si, pour une raison quelconque, la version standard de Windows ne fonctionne pas (par exemple, génère une erreur), essayez une version nocturne ( ci-dessous ).

Les builds nocturnes corrigent souvent les bogues signalés après la dernière version. ??

## macOS

- Navigateur de base de données pour SQLite [MACOS](https://download.sqlitebrowser.org/DB.for.SQLite-3.12.dmg)

#### Homebrew

Si vous préférez utiliser Homebrew pour macOS, notre dernière version peut être installée via Homebrew Cask :

```bash
brew install --cask db-browser-for-sqlite
```
## Linux

Pour la dernière version est disponible sous forme d'AppImage, de packages Snap et de packages spécifiques à la distribution :

#### AppImage

- DB_Browser_for_SQLite-v3.12.2-x86_64.AppImage [Linux](https://download.sqlitebrowser.org/B_Browser_for_SQLite-v3.12.2-x86_64.AppImage)

- Version Snap Release
  
```bash
snap install sqlitebrowser
```
- Snap Nightly
  
```bash
snap install sqlitebrowser --devmode
```

## CRUD
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

## 3 Update 
```sql
UPDATE student SET name= "mutemba", email="mutemba@gmail.com" WHERE id_s = 3
UPDATE course SET id_etr=1  WHERE id_c = 4

```
## 4 Delete 
```sql
DELETE FROM student  WHERE id_s = 3
DELETE FROM student  WHERE id_s = 1

```

