import sys
import re

input = sys.stdin.readline

T = int(input())

import re

pattern = r"(100+1+|01)+"
for _ in range(T):
    print("YES" if re.fullmatch(pattern, input()[:-1]) else "NO")
