import sys
import itertools

input = sys.stdin.readline

L, C = map(int, input().split())
alpha = input().split()
alpha.sort()

combi = list(itertools.combinations(alpha, L))

ans = []

for s in combi:
    consonant = 0
    vowel = 0
    for c in s:
        if c in ["a", "e", "i", "o", "u"]:
            consonant += 1
        else:
            vowel += 1
    if consonant >= 1 and vowel >= 2:
        for c in s:
            print(c, end="")
        print()
