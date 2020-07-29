from tabela_ir import get_aliquota_e_parcela_a_deduzir

def deducao_simplificada(salario_anual):
    return (salario_anual * 0.2)

def base_calculo(salario_anual, aliquota, parcela_dedutivel):
    base = salario_anual - deducao_simplificada(salario_anual)
    imposto_inicial = base * aliquota

    return imposto_inicial - parcela_dedutivel


def calcular_imposto_de_renda(salario_anual):
    salario_deducao_simplificada = salario_anual - deducao_simplificada(salario_anual)
    aliquota,parcela_dedutivel = get_aliquota_e_parcela_a_deduzir(salario_deducao_simplificada)

    imposto = base_calculo(salario_anual, aliquota, parcela_dedutivel)

    if(imposto > 0):
        return (f"O valor do imposto a ser pago é R${imposto:.2f}")
    else:
        return ("Isento!")
 
