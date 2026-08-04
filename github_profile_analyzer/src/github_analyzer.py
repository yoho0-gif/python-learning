def summarize_repositories(repos):
    if not repos:
        return None

    total_repos = len(repos)
    total_stars = 0
    languages = {}
    top_repo = None
    max_stars = -1

    for repo in repos:
        stars = repo.get("stargazers_count", 0)
        total_stars += stars

        lang = repo.get("language")
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

        if stars > max_stars:
            max_stars = stars
            top_repo = {
                "name": repo.get("name"),
                "stars": stars,
                "description": repo.get("description") or "無簡介"
            }

    sorted_languages = dict(
        sorted(languages.items(), key=lambda item: item[1], reverse=True)
    )

    summary = {
        "repo_count": total_repos,
        "total_stars": total_stars,
        "top_languages": sorted_languages,
        "most_starred_repo": top_repo
    }

    return summary