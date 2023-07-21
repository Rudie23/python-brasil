"""
Exercício 12 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos
os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
  Salário Bruto até 900 (inclusive) - isento
  Salário Bruto até 1500 (inclusive) - desconto de 5%
  Salário Bruto até 2500 (inclusive) - desconto de 10%
  Salário Bruto acima de 2500 - desconto de 20%

Mostrar valores monetários com duas casas decimais, alinhados à direita, com espaço para 5 dígitos de salário, ou seja,
até R$ 99999,99

    >>> calcular_salario_liquido(1, 160)
    Salário Bruto: (R$ 1.00 * 160)     : R$   160.00
    (-) IR (0%)                        : R$     0.00
    (-) INSS (10%)                     : R$    16.00
    (-) Sindicato (3%)                 : R$     4.80
    FGTS (11%)                         : R$    17.60
    Total de descontos                 : R$    20.80
    Salário Liquido                    : R$   139.20
    >>> calcular_salario_liquido(5, 220)
    Salário Bruto: (R$ 5.00 * 220)     : R$  1100.00
    (-) IR (5%)                        : R$    55.00
    (-) INSS (10%)                     : R$   110.00
    (-) Sindicato (3%)                 : R$    33.00
    FGTS (11%)                         : R$   121.00
    Total de descontos                 : R$   198.00
    Salário Liquido                    : R$   902.00
    >>> calcular_salario_liquido(10, 160)
    Salário Bruto: (R$ 10.00 * 160)    : R$  1600.00
    (-) IR (10%)                       : R$   160.00
    (-) INSS (10%)                     : R$   160.00
    (-) Sindicato (3%)                 : R$    48.00
    FGTS (11%)                         : R$   176.00
    Total de descontos                 : R$   368.00
    Salário Liquido                    : R$  1232.00
    >>> calcular_salario_liquido(100, 160)
    Salário Bruto: (R$ 100.00 * 160)   : R$ 16000.00
    (-) IR (20%)                       : R$  3200.00
    (-) INSS (10%)                     : R$  1600.00
    (-) Sindicato (3%)                 : R$   480.00
    FGTS (11%)                         : R$  1760.00
    Total de descontos                 : R$  5280.00
    Salário Liquido                    : R$ 10720.00

"""


# noinspection DuplicatedCode
def calcular_salario_liquido(valor: float, horas: float):
    salario_bruto = valor * horas
    INSS = 0.1
    SIND = 0.03
    FGTS = 0.11

    INSS_TAXA = 10
    SIND_TAXA = 3
    FGTS_TAXA = 11

    if salario_bruto <= 900:
        IR = 0
        IR_TAXA = 0

        # noinspection DuplicatedCode
        fgts_bonus = salario_bruto * FGTS
        descontos = salario_bruto * (IR + INSS + SIND)
        salario_liquido = salario_bruto - descontos

        # IR desconto
        ir_desconto = salario_bruto * IR

        # INSS desconto
        inss_desconto = salario_bruto * INSS

        # Sindicato desconto
        sind_desconto = salario_bruto * SIND

        print(f'Salário Bruto: (R$ {valor:.2f} * {horas})     : R$   {salario_bruto:.2f}\n'
              f'(-) IR ({IR_TAXA}%)                        : R$     {ir_desconto:.2f}\n'
              f'(-) INSS ({INSS_TAXA}%)                     : R$    {inss_desconto:.2f}\n'
              f'(-) Sindicato ({SIND_TAXA}%)                 : R$     {sind_desconto:.2f}\n'
              f'FGTS ({FGTS_TAXA}%)                         : R$    {fgts_bonus:.2f}\n'
              f'Total de descontos                 : R$    {descontos:.2f}\n'
              f'Salário Liquido                    : R$   {salario_liquido:.2f}')

    elif 900 < salario_bruto <= 1500:
        IR = 0.05
        IR_TAXA = 5

        fgts_bonus = salario_bruto * FGTS
        descontos = salario_bruto * (IR + INSS + SIND)
        salario_liquido = salario_bruto - descontos

        # IR desconto
        ir_desconto = salario_bruto * IR

        # INSS desconto
        inss_desconto = salario_bruto * INSS

        # Sindicato desconto
        sind_desconto = salario_bruto * SIND

        print(f'Salário Bruto: (R$ {valor:.2f} * {horas})     : R$  {salario_bruto:.2f}\n'
              f'(-) IR ({IR_TAXA}%)                        : R$    {ir_desconto:.2f}\n'
              f'(-) INSS ({INSS_TAXA}%)                     : R$   {inss_desconto:.2f}\n'
              f'(-) Sindicato ({SIND_TAXA}%)                 : R$    {sind_desconto:.2f}\n'
              f'FGTS ({FGTS_TAXA}%)                         : R$   {fgts_bonus:.2f}\n'
              f'Total de descontos                 : R$   {descontos:.2f}\n'
              f'Salário Liquido                    : R$   {salario_liquido:.2f}')

    elif 1500 < salario_bruto <= 2500:
        IR = 0.1
        IR_TAXA = 10

        fgts_bonus = salario_bruto * FGTS
        descontos = salario_bruto * (IR + INSS + SIND)
        salario_liquido = salario_bruto - descontos

        # IR desconto
        ir_desconto = salario_bruto * IR

        # INSS desconto
        inss_desconto = salario_bruto * INSS

        # Sindicato desconto
        sind_desconto = salario_bruto * SIND

        print(f'Salário Bruto: (R$ {valor:.2f} * {horas})    : R$  {salario_bruto:.2f}\n'
              f'(-) IR ({IR_TAXA}%)                       : R$   {ir_desconto:.2f}\n'
              f'(-) INSS ({INSS_TAXA}%)                     : R$   {inss_desconto:.2f}\n'
              f'(-) Sindicato ({SIND_TAXA}%)                 : R$    {sind_desconto:.2f}\n'
              f'FGTS ({FGTS_TAXA}%)                         : R$   {fgts_bonus:.2f}\n'
              f'Total de descontos                 : R$   {descontos:.2f}\n'
              f'Salário Liquido                    : R$  {salario_liquido:.2f}')

    else:
        IR = 0.2
        IR_TAXA = 20

        fgts_bonus = salario_bruto * FGTS
        descontos = salario_bruto * (IR + INSS + SIND)
        salario_liquido = salario_bruto - descontos

        # IR desconto
        ir_desconto = salario_bruto * IR

        # INSS desconto
        inss_desconto = salario_bruto * INSS

        # Sindicato desconto
        sind_desconto = salario_bruto * SIND

        print(f'Salário Bruto: (R$ {valor:.2f} * {horas})   : R$ {salario_bruto:.2f}\n'
              f'(-) IR ({IR_TAXA}%)                       : R$  {ir_desconto:.2f}\n'
              f'(-) INSS ({INSS_TAXA}%)                     : R$  {inss_desconto:.2f}\n'
              f'(-) Sindicato ({SIND_TAXA}%)                 : R$   {sind_desconto:.2f}\n'
              f'FGTS ({FGTS_TAXA}%)                         : R$  {fgts_bonus:.2f}\n'
              f'Total de descontos                 : R$  {descontos:.2f}\n'
              f'Salário Liquido                    : R$ {salario_liquido:.2f}')
