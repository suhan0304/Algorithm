import itertools

L, C = map(int, input().split())
alpha = input().split()
alpha.sort()

combi = list(itertools.combinations(alpha, L))  # 4개의 원소로 가능한 모든 조합을 생성

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
