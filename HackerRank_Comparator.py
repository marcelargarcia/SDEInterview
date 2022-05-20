#https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

import functools
from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else:
            if a.name > b.name:
                return 1
            else:
                return -1


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    player = Player(name, int(score))
    data.append(player)
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)