"""
Exercício 18 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em MBps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
Arredonde o tempo em minutos

    >>> from estrutura_sequencial import ex_18
    >>> numeros =['50', '2500']
    >>> ex_18.input = lambda k: numeros.pop()
    >>> ex_18.calcular_tempo_de_download()
    O tempo aproximado do Download é: 0.83 minuto(s)
    >>> numeros =['100', '2500']
    >>> ex_18.input = lambda k: numeros.pop()
    >>> ex_18.calcular_tempo_de_download()
    O tempo aproximado do Download é: 0.42 minuto(s)

"""


def calcular_tempo_de_download():
    arquivo_tamanho = input('Qual o tamanho do arquivo em MB? \n')
    arquivo = float(arquivo_tamanho)
    velocidade = float(input('Qual a velocidade em MBps? \n'))
    tempo_segundos = arquivo / velocidade
    min_para_seg = 60
    tempo_minutos = tempo_segundos / min_para_seg
    print(f'O tempo aproximado do Download é: {tempo_minutos:.2f} minuto(s)')


if __name__ == '__main__':
    calcular_tempo_de_download()
