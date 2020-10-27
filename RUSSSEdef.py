def saisire(ch):
    print("donner",ch,end=" ")
    a=int(input())
    while not (a > 0):
        print("donner",ch,end=" ")
        a=int(input())
    return a
def remplire(A,B,M,D):
    i = 0
    while not (D[i] == 1):
        M.append(M[i]*2)
        D.append(D[i]//2)
        i += 1
def afficher(D,M,A,B):
    S=0
    for y in range(len(D)):
        if D[y] % 2 != 0:
            S += M[y]
    print(A, '*', B, '=', S)
    
#pp
   
a=saisire("a :")
b=saisire("b :")
M=[a]
D=[b] 
remplire(a,b,M,D)
print(M)
print(D)

afficher(D,M,a,b)