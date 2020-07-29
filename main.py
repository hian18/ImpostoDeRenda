from calculos import calcular_imposto_de_renda

#main
def executar():

    salario_anual = float(input("Digite o salário anual: "))
    resultado=calcular_imposto_de_renda(salario_anual)
    print(resultado)

if(__name__ == "__main__"):
    executar()

""""
    if(aux > 4664.68):
        imposto = imposto + ((aux - 4664.68) * 0.275)
        aux = 4664.68
    if(aux <= 4664.68 and aux > 3751.06):
        imposto = imposto + ((aux - 3751.06) * 0.225)
        aux = 3751.06
    if (aux <= 3751.06 and aux > 2826.66):
        imposto = imposto + ((aux - 2826.66) * 0.15)
        aux = 2826.66
    if (aux <= 2826.66 and aux > 1903.99):
        imposto = imposto + ((aux - 1903.99) * 0.075)
        aux = 1903.99
    #o restante é isento

    return imposto
"""