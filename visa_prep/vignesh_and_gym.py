x, y, z=map(int,input().split())
if x<=z and x+y<=z:
    print("2")
elif x<=z:
    print("1")
else:
    print("0")