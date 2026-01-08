# 获取输入的运动员的实力值
tmp = list(map(int, input("请输入运动员的实力值，以空格隔开").split()))
print(tmp)

class Sport:
    def __init__(self, idx, strength):
        self.idx = idx
        self.strength = strength

# 将输入的运动员实力值转化为运动员集合
sports = []
for i in range(len(tmp)):
    sports.append(Sport(i, tmp[i]))

# 晋级赛
def promote(sports, ans):
    # 记录胜者组
    win = []
    # 记录败者组
    fail = []

    for i in range(1, len(sports), 2):
        # 每组比赛序号大的运动员
        major = sports[i]
        # 每组比赛序号小的运动员
        minor = sports[i-1]

        if major.strength > minor.strength:
            win.append(major)
            fail.append(minor)
        else:
            win.append(minor)
            fail.append(major)

        # 如果晋级赛中，运动员个数为奇数，则最后一个运动员直接晋级
        if len(sports)%2 != 0:
            win.append(sports[-1])

        # 依次头部压入失败组、胜者组
        ans.insert(0, fail)
        ans.insert(0, win)

    # 当保留组超过3个的时候，那么需要将超过部分去掉，因为这部分已经无缘季军
    while len(ans) > 3:
        ans.pop()

# 算法入口
def getresult():
    # 保留组ans只保留三个组：冠军组、亚军组和季军组
    ans = []

    # 晋级赛
    promote(sports, ans)

    # 冠军组如果还不是一个人，那么还需要取出冠军组继续进行晋级赛
    if len(ans[0]) != 1:
        promote(ans.pop(0), ans)

    # 冠军
    first = ans[0][0].idx

    # 亚军
    second = ans[1][0].idx

    # 季军
    ans[2].sort(key=lambda x: (-x.strength, x.idx))
    third = ans[2][0].idx

    return f"{first} {second} {third}"


if __name__ == "__main__":
    res = getresult()
    print(res)