def deducao_simplificada(salario_anual):
    return (salario_anual * 0.2)
    
def base_calculo(salario_anual, aliquota, parcela_dedutivel):
    base = salario_anual - deducao_simplificada(salario_anual)
    imposto_inicial = base * aliquota

    return imposto_inicial - parcela_dedutivel
