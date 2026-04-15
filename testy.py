from modul_git import przygotuj_liste_zmian
import os


REPO = os.path.dirname(os.path.abspath(__file__))
def test_zwraca_liste():
    wynik = przygotuj_liste_zmian(REPO, "HEAD~1", "HEAD")
    assert isinstance(wynik, list)
def test_commit_ma_klucze():
    wynik = przygotuj_liste_zmian(REPO, "HEAD~1", "HEAD")
    if len(wynik) > 0:
        assert "hash" in wynik[0]
        assert "wiadomosc" in wynik[0]
        assert "autor" in wynik[0]
        assert "diff" in wynik[0]


def test_pusta_lista_gdy_zły_zakres():
    wynik = przygotuj_liste_zmian(REPO, "HEAD", "HEAD")
    assert wynik == []