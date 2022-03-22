import numpy as np
from scipy.stats import mode
from scipy.stats import trim_mean
from scipy.stats import skew

import matplotlib.pyplot as plt

# >>>> Exemplo de cálculo de frequência
banda = np.array(['Fresno', 'Cuscobayo', 'Fresno', 'Fresno',
                 'Cuscobayo', 'Fresno', 'Fresno', 'Maglore'])
# Calcular a frequencia da categoria banda no atributo Fresno
frequencia = (banda == 'Fresno').sum() / float(banda.size)
print('Frequência da categoria "Fresno" é ', frequencia)

# Calcular moda
moda, quantidade = mode(banda)
print('A moda é a categoria "{}". Quantidade de repetições: {}'.format(
    moda[0], quantidade))

listNumeros = np.array([5, 40, 1, 13, 18, 15, 13, 14])

# Calcular a média
print('A média é ', np.mean(listNumeros))

# Calcular a mediana
print('A mediana é ', np.median(listNumeros))

# Calcular média Podada
# Ela minimiza problema da média (outliers) descartando valores dos extremos
# Eliminar 20% (0.2) dos valores em cada extremidade
print('A média podada é ', trim_mean(listNumeros, 0.2))

# Calcular Percentil
print('O percentil 50% é ', np.percentile(listNumeros, 50))

# Boxplot
#      Q1-1.5IQR   Q1   median  Q3   Q3+1.5IQR
#                   |-----:-----|
#   o      |--------|     :     |--------|    o  o
#                   |-----:-----|
# flier             <----------->            fliers
#                        IQR
plt.boxplot(listNumeros)
# plt.show()

# Calculo de intervalo
# Sofre com outliers
print('O intervalo é ', listNumeros.max() - listNumeros.min())

# variancia
# Medida preferida para análise de espelhamento
print('A variancia com correção de Bessel é ', round(listNumeros.var(ddof=1), 2))
print('A variancia sem correção de Bessel é ', round(listNumeros.var(), 2))

# Desvio padrão
print('O desvio padrão com correção de Bessel é ', round(listNumeros.std(ddof=1), 2))
print('O desvio padrão correção de Bessel é ', round(listNumeros.std(), 2))

# Obliquidade (skew): mede a simetria da distribuição em torno da média
# Para normalização bias=True
print('A obliquidade é ', round(skew(listNumeros, bias=True), 3))
