from git import repo, Repo


def pobierz_commity(sciezka_repo, od_tag, do_tag):
    repo = Repo(sciezka_repo)
    zakres = f"{od_tag}-{do_tag}"
    commity = list(repo.iter_commits(zakres))
    return commity