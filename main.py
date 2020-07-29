from tabela_ir import get_aliquota_e_parcela_a_deduzir
from calculos import base_calculo

#main
def executar(salario_anual):

    aliquota,parcela_dedutivel = get_aliquota_e_parcela_a_deduzir(salario_anual)

    imposto = base_calculo(salario_anual, aliquota, parcela_dedutivel)

    if(imposto > 0):
        print(f"O valor do imposto a ser pago é R${imposto:.2f}")
    else:
        print("Isento!")

if(__name__ == "__main__"):
    salario_anual = float(input("Digite o salário anual: "))
    executar(salario_anual)

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