while True:
    try:
        s = input()
        ans = [0] * 4
        for c in s:
            if c.islower():
                ans[0] += 1
            elif c.isupper():
                ans[1] += 1
            elif c.isnumeric():
                ans[2] += 1
            elif c.isspace():
                ans[3] += 1
        print(" ".join(map(str, ans)))

    except:
        break
