import numpy as np

## >>>> Exemplo de cálculo de frequência
banda = np.array(['Fresno', 'Cuscobayo', 'Fresno', 'Fresno', 'Cuscobayo', 'Fresno', 'Fresno', 'Maglore' ])
# Calcular a frequencia da categoria banda no atributo Fresno
frequencia = (banda == 'Fresno').sum() / float(banda.size)
print ('Frequência da categoria "Fresno" é ', frequencia)
