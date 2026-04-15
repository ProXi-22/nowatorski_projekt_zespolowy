import argparse
from modul_git import przygotuj_liste_zmian
from modul_llm import generuj_release_notes
from datetime import date

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

release_notes = generuj_release_notes(lista_zmian)

nazwa_repo = argumenty.repo.rstrip("/").split("/")[-1]
nazwa_pliku = f"release_notes_{nazwa_repo}_{date.today()}.md"

with open(nazwa_pliku, "w", encoding="utf-8") as plik:
    plik.write(release_notes)

print(f"Zapisano: {nazwa_pliku}")