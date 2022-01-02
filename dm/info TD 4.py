## exercice 1.1
def appartient (e,L):
    for i in range (len(L)):
        if L[i]==e:
            return True
    return False

##1.2
#1 comaraison
#4 comparaisons
#3 comaraisons

##1.3
#minimum 1 comparaison / maximum n comparaisons

##1.4
# 10**11/10**9=100 donc pour une liste de taille 10**11, l'execution de appartient prendrait au plus 1min et 40 secondes.


## exercice 2
def croissant(L):
    for i in range (len(L)-1):
        if L[i]>L[i+1]:
            return False
    return True


##exercice 3
#sur cet exemple, il y a 3 comparaisons par dichotomie, alors qu'avec appartient, il y en a 11. La méthode par dichotomie semble être la plus efficace.


##exercice 4
def dichotomie(e, L):
    i, j = 0, len(L) - 1  # i et j sont les indices de L entre lesquels on cherche e
    while i!=j: # tant qu'il reste au moins 1 élément entre les indices i et j
        m =(i+j)//2 # milieu de i et j
        if e < L[m]:
            i,j=0,m# regarder dans la partie gauche
        elif e > L[m]:
            i,j=m,j # regarder dans la partie droite
        else:
            return m # on a trouvé e
    return "e n'est pas dans L" # e n'a pas été trouvé



##exercice 5
#log(10**11)/10**9=11/9=1,2
#l'exécution de dichotomie pour une liste de taille 10**11 sur un ordinateur de 1 GHz prendrait environ 1,2 seconde.


##exercice 6
def puissance(a,n):
    p=1
    for i in range (n):
        p=a*p
    return p


##exercice 7.1:
#1er passage: r=1; a=4; n=6
#2e passage: r=1; a=16; n=3
#3e passage: r=16; a=256; n=1
#4e passage: r=4096; a=65536; n=0

##7.2
#puissance_rapide(2,12) réalise 6 multiplications alors que puissnce(2,12) en réalisait 12.

##7.3
#soit r_0 ; a_0 et n_0 les les variables r a et n au passage 0 dans while, et r_1 ; a_1 et n_1 leurs valeurs après leur passage 0+1 dans la boucle.
#Si n_0 est impaire:
#r_1*(a_1**n_1)= r_0*a_0*(a_0**n-1)= r_0*(a_0**n_0)

#si n_0 est pair:
#r_1*(a_1**n_1)= r_0*(a_0**n_0)

#Au total, on remarque que la valeur de r*(a**n) ne change pas, ainsi lorsque n=0, on a bien r qui prend la valeur de a**n.(car r initialement vaut 1)


##7.4




