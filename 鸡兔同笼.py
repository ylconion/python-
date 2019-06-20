a, b = map(int,input().split())
c = (b-2*a)/2
d = a-c
if d < 0 or c < 0 or d%1 != 0 or c%1 != 0:
    print("Data Error!")
else:
    print(int(d), int(c))
