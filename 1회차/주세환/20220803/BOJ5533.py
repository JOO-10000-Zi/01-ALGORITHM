from pprint import pprint
N = int(input())

scores = [[], [], []]
for _ in range(N):
    a, b, c = map(int, input().split())
    scores[0].append(a)
    scores[1].append(b)
    scores[2].append(c)

player_ = [0] * N
for i in range(3):
    for j in range(N):
        if scores[i].count(scores[i][j]) >= 2:
            player_[j] += 0
        else:
            player_[j] += scores[i][j]
for s in player_:
    print(s)