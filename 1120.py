import sys

input = sys.stdin.readline

a, b = input().strip().split()

if a in b:
    print(0)
elif len(a) == len(b):
    print(sum(1 for i in range(len(a)) if a[i] == b[i]))
else:
    b_1 = a + b[len(a) :]
    b_2 = b[: len(b) - len(a)] + a
    print(
        min(
            sum(1 for i in range(len(a)) if b_1[i] != b[i]),
            sum(1 for i in range(len(a)) if b_2[i] != b[i]),
        )
    )
