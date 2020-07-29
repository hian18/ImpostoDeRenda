SALARIO_MAXIMO = 9999999

#salario anual min, salario anual max, aliquota, parcela dedutivel
TABELA_IR_ANUAL_2020 = (
    (0, 22847.76, 0, 0),
    (22847.77, 33919.80, 0.075, 1713.58),
    (33919.81, 45012.60, 0.15, 4257.57),
    (45012.61, 55976.16, 0.225, 7633.51),
    (55976.16, SALARIO_MAXIMO, 0.275, 10432.32),
)

#retorna a aliquota e a parcela a deduzir
def get_aliquoto_e_parcela_a_deduzir(salario: float)->tuple:
    salario = salario - deducao_simplificada(salario)

    for linha in TABELA_IR_ANUAL_2020:
        if linha[0] <= salario <= linha[1]:
            return linha[-2], linha[-1]

def deducao_simplificada(salario_anual):
    return (salario_anual * 0.2)

