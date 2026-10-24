import csv
import os
from config import EXPORT_DIR, FICHIER_EXPORT

class ExportView:
    def vers_csv(self, produits):
        os.makedirs(EXPORT_DIR, exist_ok=True)
        chemin = os.path.join(EXPORT_DIR, FICHIER_EXPORT)
        with open(chemin, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["titre", "prix", "note", "url"])
            for p in produits:
                w.writerow([p.titre, p.prix, p.note, p.url])
        return chemin