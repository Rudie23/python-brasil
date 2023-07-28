"""
Exercício 05 da seção de strings da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

    >>> inverter_escada('CAMARGUINHO')
    CAMARGUINHO
    CAMARGUINH
    CAMARGUIN
    CAMARGUI
    CAMARGU
    CAMARG
    CAMAR
    CAMA
    CAM
    CA
    C
    >>> inverter_escada('ENZO_PASCOAL')
    ENZO_PASCOAL
    ENZO_PASCOA
    ENZO_PASCO
    ENZO_PASC
    ENZO_PAS
    ENZO_PA
    ENZO_P
    ENZO_
    ENZO
    ENZ
    EN
    E

"""


def inverter_escada(nome: str):
    """Escreva aqui em baixo a sua solução"""
    tamanho = len(nome)
    s = nome

    for i in range(1, tamanho + 1):
        print(nome)
        nome = s[:-i]


if __name__ == '__main__':
    inverter_escada('casa')
