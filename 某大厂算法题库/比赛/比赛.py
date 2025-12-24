from functools import cmp_to_key

# 输入评委人数和参赛选手人数
m, n = map(int, input("请输入评委人数和参赛人数(以英文逗号隔开，如4,5): ").split(','))
scores = [list(map(int, input("请输入评委打分(以英文逗号隔开): ").split(','))) for _ in range(m)]


def cmp(a, b):
    if a["sum"] != b["sum"]:
        return b["sum"] - a["sum"]

    for i in range(m):
        if a["score"][i] == b["score"][i]:
            continue
        return b["score"][i] - a["score"][i]
    return 0


def getresult():
    if m < 3 or m > 10 or n < 3 or n > 100:
        return "-1"

    players = []

    for j in range(n):
        player = []
        for i in range(m):
            if scores[i][j] < 1 or scores[i][j] > 10:
                return "-1"
            player.append(scores[i][j])
        player.sort(reverse=True)
        players.append({
            "idx": j,
            "sum": sum(player),
            "score": player
        })
    sorted_players = sorted(players, key=cmp_to_key(cmp))

    return ",".join(list(map(lambda x: str(x["idx"] + 1), sorted_players[:3])))


print(getresult())
