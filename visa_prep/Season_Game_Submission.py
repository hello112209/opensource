x=int(input())
if 1<=x<=12:
    if 3<=x<=5:
        print("Spring")
    elif 6<=x<=8:
        print("Summer")
    elif 9<=x<=11:
        print("Autumn")
    else:
        print("Winter")
else:
    print("Invalid")
