

SQLite est une bibliothèque écrite en langage C qui propose un moteur de base de données relationnelle accessible par le langage SQL. SQLite implémente en grande partie le standard SQL-92 et des propriétés ACID.

Contrairement aux serveurs de bases de données traditionnels, comme MySQL ou PostgreSQL, sa particularité est de ne pas reproduire le schéma habituel client-serveur mais d'être directement intégrée aux programmes. L'intégralité de la base de données (déclarations, tables, index et données) est stockée dans un fichier indépendant de la plateforme.

D. Richard Hipp, le créateur de SQLite, a choisi de mettre cette bibliothèque ainsi que son code source dans le domaine public, ce qui permet son utilisation sans restriction aussi bien dans les projets open source que dans les projets propriétaires. Le créateur ainsi qu'une partie des développeurs principaux de SQLite sont employés par la société américaine Hwaci2.

SQLite est le moteur de base de données le plus utilisé au monde, grâce à son utilisation :

dans de nombreux logiciels grand public comme Firefox, Skype, Google Gears,

dans certains produits d'Apple, d'Adobe et de McAfee,

dans les bibliothèques standards de nombreux langages comme PHP ou Python.

De par son extrême légèreté (moins de 600 Kio3), il est également très populaire sur les systèmes embarqués, notamment sur la plupart des smartphones et tablettes modernes : les systèmes d'exploitation mobiles iOS, Android et Symbian l'utilisent comme base de données embarquée4. Au total, on peut dénombrer plus d'un milliard de copies connues et déclarées de la bibliothèque5.


# crud
1.

CREATE TABLE student (
	id	INTEGER,
	name	varchar(10), 
	lastname	varchar(15),
	email	varchar(20),
	phone1 varchar(20),
	PRIMARY KEY("id" AUTOINCREMENT)
)
