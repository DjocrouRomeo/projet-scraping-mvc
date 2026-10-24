import sqlite3
from config import DB_PATH
from app.models.produit import Produit

class Depot:
    def __init__(self, chemin=DB_PATH):
        self.connexion = sqlite3.connect(chemin)
        self.connexion.execute(
            """CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre TEXT NOT NULL UNIQUE,
                prix TEXT,
                note TEXT,
                url TEXT
            )"""
        )
        self.connexion.commit()

    def ajouter(self, produit):
        self.connexion.execute(
            "INSERT OR IGNORE INTO produits (titre, prix, note, url) VALUES (?, ?, ?, ?)",
            (produit.titre, produit.prix, produit.note, produit.url),
        )
        self.connexion.commit()

    def ajouter_plusieurs(self, produits):
        for p in produits:
            self.ajouter(p)

    def tous(self):
        lignes = self.connexion.execute("SELECT titre, prix, note, url FROM produits ORDER BY id").fetchall()
        return [Produit(*ligne) for ligne in lignes]

    def taille(self):
        return self.connexion.execute("SELECT COUNT(*) FROM produits").fetchone()[0]

    def fermer(self):
        self.connexion.close()