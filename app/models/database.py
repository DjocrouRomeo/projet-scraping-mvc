import sqlite3
import os
from config import DB_PATH


class DatabaseModel:
    def __init__(self):
        # S'assure que le dossier data existe
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        self.creer_table()

    def connecter(self):
        """Établit la connexion avec la base de données SQLite."""
        return sqlite3.connect(DB_PATH)

    def creer_table(self):
        """Crée la table des produits si elle n'existe pas déjà."""
        conn = self.connecter()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre TEXT,
                prix TEXT,
                note TEXT,
                categorie TEXT,
                image_url TEXT,
                image_path_locale TEXT
            )
        """)
        conn.commit()
        conn.close()

    def sauvegarder_produits(self, produits):
        """Insère une liste de produits en base de données."""
        if not produits:
            return 0

        conn = self.connecter()
        cursor = conn.cursor()

        data = [
            (
                p.get("titre"),
                p.get("prix"),
                p.get("note"),
                p.get("categorie"),
                p.get("image_url"),
                p.get("image_path_locale")
            )
            for p in produits
        ]

        cursor.executemany("""
            INSERT INTO produits (titre, prix, note, categorie, image_url, image_path_locale)
            VALUES (?, ?, ?, ?, ?, ?)
        """, data)

        conn.commit()
        nb_inseres = cursor.rowcount
        conn.close()
        return nb_inseres