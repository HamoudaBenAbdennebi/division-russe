def saisir():
    x=int(input("donnez un entier : "))
    while x<=0 :
        x=int(input("donnez un entier : "))
    return x
def remplir(A,B,M,D):
    M.append(A)
    D.append(B)
    i=0
    while D[i]!=1:
        M.append(M[i]*2)
        D.append(D[i]//2)
        i+=1
def somme(M,D):
    s=0
    i=0
    for x in D:
        if (x%2!=0):
            s+=M[i]
        i+=1
    return s

    3
#pp
M=[]
D=[]
A=saisir()
B=saisir()
remplir(A,B,M,D)
s=somme(M,D)
print(M)
print(D)
print(A,"X",B,"=",s)


