from random import randint, shuffle
import matplotlib as mpl
import timeit


Dlista = [10000, 20000, 30000, 40000, 50000]


def geraLista(tam):
    lista = []
    for i in range(tam):
        lista.append(randint(0,tam))
    shuffle(lista)

    return lista


def radixsort(lista):
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True

        buckets = [list() for _ in range(RADIX)]


        for i in lista:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False


        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                lista[a] = i
                a += 1


        placement *= RADIX

mpl.use('Agg')
import matplotlib.pyplot as plt
def desenhaGrafico(x,y,ym,yp,xl = "Tamanho", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Pior Tempo")
    ax.plot(x,ym, label = "Melhor Tempo")
    ax.plot(x,yp, label = "Medio Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('GraficoRadix.png')

MelhorCaso = []
PiorCaso = []
MedioCaso = []

for i in Dlista:
    medio = geraLista(i)
    melhor = sorted(medio)
    pior = sorted(melhor, reverse=True)

    MelhorCaso.append(timeit.timeit("aux={}\naux = radixsort(aux)".format(melhor.copy()),setup="from __main__ import radixsort",number=1))
    PiorCaso.append(timeit.timeit("aux={}\naux = radixsort(aux)".format(pior.copy()),setup="from __main__ import radixsort",number=1))
    MedioCaso.append(timeit.timeit("aux={}\naux = radixsort(aux)".format(medio.copy()),setup="from __main__ import radixsort",number=1))
    print("Ordenado um i em Dlista!")


desenhaGrafico(Dlista,MedioCaso,MelhorCaso,PiorCaso)

import itertools as it
tamlista = list(it.permutations(list(range(6))))
tempoIteracao = []
listaOrig = []
for lista in tamlista:
    tempoIteracao.append(timeit.timeit("radixsort({})".format(list(lista).copy()),setup="from __main__ import radixsort",number=1))
    listaOrig.append(list(lista))

print("O tempo minimo foi de {}".format(min(tempoIteracao)))
print("lista que teve tempo minimo foi:{}".format(listaOrig[tempoIteracao.index(min(tempoIteracao))]))
print("O tempo maximo foi de {}".format(max(tempoIteracao)))
print("lista que teve tempo maximo foi:{}".format(listaOrig[tempoIteracao.index(max(tempoIteracao))]))


