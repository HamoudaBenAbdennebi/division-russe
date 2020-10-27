import numpy as np

def saisire(ch):
    print("donner",ch,end=" ")
    a=int(input())
    while not (a > 0):
        print("donner",ch,end=" ")
        a=int(input())
    return a
def remplire(a,b,M,D):
    M[0]=a
    D[0]=b
    i = 0
    while not (D[i] == 1):
        i+=1
        M[i]=(M[i-1]*2)
        D[i]=(D[i-1]//2)
        
def afficher(D,M,A,B):
    S=0
    for y in range(len(D)):
        if D[y] % 2 != 0:
            S += M[y]
    print(A, '*', B, '=', S)
    
    
a=saisire("a :")
b=saisire("b :")
M=np.zeros((10),dtype=int)
D=np.zeros((10),dtype=int)
remplire(a,b,M,D)
print(M)
print(D)

afficher(D,M,a,b)