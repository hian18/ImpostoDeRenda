import tabela_ir

def base_calculo(salario_anual, aliquota, parcela_dedutivel):
    base = salario_anual - deducao_simplificada(salario_anual)
    imposto_inicial = base * aliquota

    return imposto_inicial - parcela_dedutivel

def deducao_simplificada(salario_anual):
    return (salario_anual * 0.2)

#main
def executar():

    salario_anual = float(input("Digite o salário anual: "))

    aliquota = tabela_ir.get_aliquoto_e_parcela_a_deduzir(salario_anual)[0]

    parcela_dedutivel = tabela_ir.get_aliquoto_e_parcela_a_deduzir(salario_anual)[1]

    imposto = base_calculo(salario_anual, aliquota, parcela_dedutivel)

    if(imposto > 0):
        print(f"O valor do imposto a ser pago é R${imposto:.2f}")
    else:
        print("Isento!")

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