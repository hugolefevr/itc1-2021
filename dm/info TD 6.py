import matplotlib.pyplot as plt
def segment(p, q):
    plt.plot([p[0], q[0]], [p[1], q[1]]);
plt.show()

##

import numpy as np
X, Y = [], []
for i in range(100):
    X.append(i*0.1)
    Y.append(X[i] + np.cos(X[i]))
plt.axis("equal")
plt.plot(X, Y);
plt.show()

##

def rotation1(r, d, a):
    print(1)
    x2 = r[0] + d * np.cos(a)
    print(x2)
    y2 = r[1] + d * np.sin(a)
    Z = (x2, y2)
    return x2, y2

##

def rotation2(r, d, a):

    x2 = r[0] + d * np.cos(a)
    y2 = r[1] + d * np.sin(a)
    Z = (x2, y2)
    segment(r, Z)
    return Z
plt.show()

##

def arbre(r, d, a, n):
    if n == 0: # cas de base : on arrête les appels récursifs
        return
    Z = rotation2(r, d, a) # dessiner le tronc
    arbre(Z, d/1.2, a-np.pi/6, n-1) # dessiner le sous-arbre droit
    arbre(Z, d/1.2, a+np.pi/6, n-1 ) # dessiner le sous-arbre gauche

plt.show()