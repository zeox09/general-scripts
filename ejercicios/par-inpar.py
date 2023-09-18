# exercicio par ou impar em python
def par_impar(number):
    residuo = number % 2
    if residuo == 0:
        print("o numero que voce ingreso e par")
    else:
        print("o numero que voce ingreso e impar")


par_impar(15)
