import math

def trouver_rationnel(x, y):

    if x >= y:
        raise ValueError(f"On doit avoir x < y. Ici x={x}, y={y}.")

    # --- Étape 1 : trouver n ∈ ℕ* tel que n(y-x) > 1 ---
    n = 1
    while n * (y - x) <= 1:
        n += 1
    # ici on a bien n(y-x) > 1

    print(f"\n{'='*55}")
    print(f"  DENSITÉ DE Q DANS R  —  Preuve constructive")
    print(f"{'='*55}")
    print(f"\n  Données : x = {x},  y = {y}")
    print(f"  y - x = {y - x}")
    print(f"\n[Étape 1] Théorème d'Archimède :")
    print(f"  On cherche n ∈ ℕ* tel que n·(y-x) > 1")
    print(f"  → n = {n},  n·(y-x) = {n * (y - x):.6f} > 1  ✓")

    # --- Étape 2 : trouver m ∈ ℤ tel que m-1 ≤ nx < m ---
    nx = n * x
    m = math.floor(nx) + 1

    print(f"\n[Étape 2] Encadrement de nx :")
    print(f"  nx = {n}·{x} = {nx:.6f}")
    print(f"  On prend m = ⌊nx⌋ + 1 = {math.floor(nx)} + 1 = {m}")
    print(f"  Vérification : m-1 = {m-1} ≤ nx = {nx:.6f} < m = {m}  ✓")

    # --- Étape 3 : vérifier x < m/n < y ---
    rationnel = m / n

    print(f"\n[Étape 3] Le rationnel candidat est  r = m/n = {m}/{n} = {rationnel:.10f}")
    print(f"\n  Vérification :")
    print(f"    x = {x:.10f}")
    print(f"    r = {rationnel:.10f}   ← rationnel trouvé")
    print(f"    y = {y:.10f}")

    assert x < rationnel < y, "Erreur : le rationnel n'est pas strictement entre x et y !"

    print(f"\n  ✅  x < m/n < y  est vérifié !")
    print(f"  Le rationnel  r = {m}/{n}  est bien compris entre {x} et {y}.")
    print(f"{'='*55}\n")

    return rationnel

# ── Interface utilisateur ─────────────────────────────────
print("╔══════════════════════════════════════════════════╗")
print("║   Densité de Q dans R  (Théorème §1.4.2)        ║")
print("╚══════════════════════════════════════════════════╝")
print("Entrez deux nombres réels x et y avec x < y.\n")

while True:
    try:
        x = float(input("  x = "))
        y = float(input("  y = "))
        trouver_rationnel(x, y)
        break
    except ValueError as e:
        print(f"  ⚠️  Erreur : {e}. Veuillez recommencer.\n")