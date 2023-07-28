"""
Exercício 03 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que receba 4 notas, mostre as notas e a média na tela.

    >>> mostrar_notas_e_media([0, 1, 2, 3])
    'Notas: 0, 1, 2, 3. Média: 1.5'
    >>> mostrar_notas_e_media([10, 14, 16, 26])
    'Notas: 10, 14, 16, 26. Média: 16.5'

"""


def mostrar_notas_e_media(inteiros: list) -> str:
    """Escreva aqui em baixo a sua solução"""
    lista_str = [str(inteiro) for inteiro in inteiros]
    print("'Notas: ", end="")
    for nota in lista_str:
        if nota == lista_str[-1]:
            print(f"{nota}. ", end="")
        else:
            print(f"{nota}, ", end="")
    print(f"Média: {(sum(inteiros)) / len(inteiros)}'")


if __name__ == '__main__':
    lista = [0, 1, 2, 3]
    mostrar_notas_e_media(lista)
