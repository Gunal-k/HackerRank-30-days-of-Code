d1,m1,y1 = map(int,input().split())
d2,m2,y2 = map(int,input().split())

fine = 0
if y1-y2 > 0:
    fine += 10000
elif y1-y2 == 0:
    if m1-m2 > 0:
        fine += 500 * (m1-m2)
    elif d1-d2 > 0:
        fine += 15 * (d1 -d2)

print(fine)