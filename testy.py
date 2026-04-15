from modul_git import przygotuj_liste_zmian
import os


REPO = os.path.dirname(os.path.abspath(file))
def test_zwraca_liste():
    wynik = przygotuj_liste_zmian(REPO, "HEAD~1", "HEAD")
    assert isinstance(wynik, list)
def test_commit_ma_klucze():












def test_pusta_lista_gdy_zły_zakres():