import sqlite3

conn = sqlite3.connect('testbase.db')   ##Connexion a la db

cursor = conn.cursor()      ##Récupère un curseur pour faire des modifications

cursor.execute("""
CREATE TABLE IF NOT EXISTS eleves (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        nom TEXT
        prenom TEXT
        classe TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS matieres (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        matiere TEXT
        option TEXT
)
""")

cursor.executemany("""
INSERT INTO matieres (matiere, option) VALUES ("Mathématiques", "commun");
INSERT INTO matieres (matiere, option) VALUES ("Physique-Chimie","commun");
INSERT INTO matieres (matiere, option) VALUES ("SVT","commun");
INSERT INTO matieres (matiere, option) VALUES ("Philosophie","commun");
INSERT INTO matieres (matiere, option) VALUES ("Histoire-Géo","commun");
INSERT INTO matieres (matiere, option) VALUES ("Anglais", "lv1");
INSERT INTO matieres (matiere, option) VALUES ("Espagnol", "lv1");
INSERT INTO matieres (matiere, option) VALUES ("Allemand", "lv1");
INSERT INTO matieres (matiere, option) VALUES ("Anglais", "lv2");
INSERT INTO matieres (matiere, option) VALUES ("Espagnol", "lv2");
INSERT INTO matieres (matiere, option) VALUES ("Allemand", "lv2");
INSERT INTO matieres (matiere, option) VALUES ("ISN", "spe");
INSERT INTO matieres (matiere, option) VALUES ("Maths", "spe");
INSERT INTO matieres (matiere, option) VALUES ("SVT", "spe");
INSERT INTO matieres (matiere, option) VALUES ("Physique", "spe");
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS matel (
        idel INTEGER
        idmat INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
        idmat INTEGER
        note REAL
        base INTEGER DEFAULT 20
)
""")

conn.commit()           ##Valide les modifications (effectue une sauvegarde)
