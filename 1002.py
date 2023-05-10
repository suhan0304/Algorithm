n = input()
for i in range(n) :
    x1, y1, r1, x2, y2, r2 = input().split()
    r3 = (int(x1)-int(x2))**2 + (int(y1)-int(y2)**2)
    print(r3)
