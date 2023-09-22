# en este script de python se creará un codigo para calcular el indice de masa muscular IMC
def calcular_imc(altura, peso):
    imc = peso/(altura**2)
    if imc <= 16:
        print("Você se enquadra na categoria magreza severa, uma visita ao médico é recomendada")
    elif imc > 16 and imc < 17:
        print("Você está dentro da categoria magreza moderada, uma visita ao médico é recomendada")
    elif imc > 17 and imc < 18.49:
        print(
            "Você está dentro da categoria magreza leve, uma visita ao médico é recomendada")
    elif imc > 18.5 and imc < 24.99:
        print(
            "Você está dentro do peso normal, recomenda-se continuar com hábitos saudáveis")
    elif imc > 25 and imc < 29.99:
        print("você está dentro da categoria acima do peso, uma visita ao médico é recomendada")
    elif imc > 30 and imc < 34.99:
        print("você está dentro da categoria Obesidade grau um, uma visita ao médico é recomendada")
    elif imc > 35 and imc < 39.99:
        print("você está dentro da categoria Obesidade grau dois, uma visita ao médico é recomendada")
    elif imc > 40:
        print("você está dentro da categoria Obesidade grau três, uma visita ao médico é recomendada")


altura = float(input(
    "Digite sua altura em metros separando os centímetros por vírgula: exemplo 172 cm => 1,72 m "
))
peso = float(input("Insira seu peso em kg "))
calcular_imc(altura, peso)
