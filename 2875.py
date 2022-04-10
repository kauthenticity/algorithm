n, m, k = map(int, input().split())


def getTeam(n, m, k):
    teams = 0

    for girlIntern in range(k+1):
        boyIntern = k-girlIntern
        if boyIntern > k:
            continue

        girlTeam = n - girlIntern
        boyTeam = m - boyIntern

        teams = max(teams, min(girlTeam//2, boyTeam))

    return teams


print(getTeam(n, m, k))
