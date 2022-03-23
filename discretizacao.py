import numpy as np
import matplotlib.pyplot as plt

data = np.array([0, 1, 2, 6, 6, 9, 10, 10, 10, 13, 18, 20, 21, 21, 25])

#histograma com larguras iguais
n, bins, patches = plt.hist(data, edgecolor='black')
plt.show()


def equalObs(x, nbin):
    nlen = len(x)
    return np.interp(np.linspace(0, nlen, nbin + 1),
                     np.arange(nlen),
                     np.sort(x))

#histograma de frequencia igual
n, bins, patches = plt.hist(data, equalObs(data, 10), edgecolor='black')
plt.show()
