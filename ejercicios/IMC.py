# en este script de python se creará un codigo para calcular el indice de masa muscular IMC
def calcular_imc(altura, peso):
    imc = peso/(altura**2)
    return imc


print(calcular_imc(1.72, 68))
