import math
x,n=map(int,input().split())
rem=n-(x*100)
planes=math.ceil(rem/100)
print(planes)
