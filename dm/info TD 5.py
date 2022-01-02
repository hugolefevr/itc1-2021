## exercice 1

# Ce code affiche les entiers croissants de 1 à n

## exercice 2

def f(n):
    if n == 0:
        return
    for i in range (n):
        print("*", end="")
    print()
    f(n-1)

## exercice 3

def f2(n):
    if n == 0:
        return
    f2(n-1)
    for i in range (n):
        print("*", end="")
    print()

n = int(input("valeur de n: "))
f2(n)
f(n)

## exercice 4

def somme(n):
    S = 0
    for i in range(n+1):
        S +=  i**2
    return S

## exercice 5

# 1. n! = (n-1)! * n

def fact(n):
    if n == 0:
        return 1
    else :
        return fact(n-1)*n

## exercice 6

def dichotomie(e, L):
    i, j = 0, len(L) - 1
    if i <= j:
        m = (i+j)//2
        if e < L[m]:
            return dichotomie(e, L[:m])
        elif e >L[m]:
            return dichotomie(e, L[m+1:])
        else:
            return True
    return False


























