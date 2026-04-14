import os
import tempfile
from git import Repo

def pobierz_repo(zrodlo):
    if zrodlo.startswith("http"):
        folder_tymczasowy = tempfile.mkdtemp()
        print(f"Klonowanie repozytorium z: {zrodlo}")
        repo = Repo.clone_from(zrodlo, folder_tymczasowy)
        return repo, folder_tymczasowy
    else:
        return Repo(zrodlo), zrodlo

def pobierz_diff(commit):
    if not commit.parents:
        return ""
    roznice = commit.diff(commit.parents[0], create_patch=True)
    tekst_diffa = ""
    for r in roznice:
        tekst_diffa += r.diff.decode("utf-8", errors="ignore")
    return tekst_diffa

def przygotuj_liste_zmian(zrodlo, od_taga, do_taga):
    repo, _ = pobierz_repo(zrodlo)
    zakres = f"{od_taga}...{do_taga}"
    commity = list(repo.iter_commits(zakres))
    lista_zmian = []
    for c in commity:
        zmiana = {
            "hash": str(c.hexsha)[:7],
            "wiadomosc": c.message.strip(),
            "autor": str(c.author),
            "diff": pobierz_diff(c)
        }
        lista_zmian.append(zmiana)
    return lista_zmian