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
