

"""
Exercício 01 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosFuncoes


"""


def piramide(n: int):
    for i in range(1, n + 1):
        for _ in range(i):
            print(i, end="   ")
        print()


if __name__ == '__main__':
    piramide(3)
