import sys
import itertools

input = sys.stdin.readline

L, C = map(int, input().split())
alpha = sorted(list(map(str, input().split())))

answer = []


def back_tracking(deep, idx):
    if deep == L:
        consonant = 0
        vowel = 0

        for c in answer:
            if c in ["a", "e", "i", "o", "u"]:
                consonant += 1
            else:
                vowel += 1

        if consonant >= 1 and vowel >= 2:
            print("".join(answer))
        return

    for i in range(idx, C):
        answer.append(alpha[i])
        back_tracking(deep + 1, i + 1)
        answer.pop()


back_tracking(0, 0)
