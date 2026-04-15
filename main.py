import argparse
from modul_git import przygotuj_liste_zmian

parser = argparse.ArgumentParser()
parser.add_argument("--repo", required=True)
parser.add_argument("--od", required=True)
parser.add_argument("--do", required=True)
argumenty = parser.parse_args()

lista_zmian = przygotuj_liste_zmian(argumenty.repo, argumenty.od, argumenty.do)

if not lista_zmian:
    print("Nie znaleziono commitow w podanym zakresie.")
    exit()

print(f"Znaleziono {len(lista_zmian)} commitow.\n")
print("Generowanie release notes...")

