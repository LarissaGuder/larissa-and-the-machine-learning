import numpy as np
from scipy.stats import mode

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

listNumeros = [5, 40, 1, 13, 18, 15, 13, 14]

# Calcular a média
print('A média é ', np.mean(listNumeros))

# Calcular a mediana
print('A mediana é ', np.median(listNumeros))
