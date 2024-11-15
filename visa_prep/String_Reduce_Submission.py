n=input()
string=""
c=1
for i in range(1, len(n)):
    if n[i]==n[i-1]:
        c=c+1
    else:
        string=string+n[i-1]+str(c)
        c=1
string=string+n[-1]+str(c)
print(string)
    
