# -*- coding: utf-8 -*-

# ==============================================================================
# title           :util.py
# description     :Biblioteca de funcoes e classes para ganho de produtividade em tarefas repetitivas
# author          :MuriloCunha
# date            :20181018
# version         :1.0
# usage           :python util.py
# notes           :
# python_version  :3.6
# ==============================================================================


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    # Estilos
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    # Voltar ao normal
    END = '\033[0m'


def desenharquadrado(larg, alt):
    print(larg * "#" + "\n"                                 # Borda Superior
          + (alt - 2) * ("#" + (larg - 2) * " " + "#\n")    # Parte Meio
          + larg * "#" + "\n")                              # Borda Inferior


if __name__ == '__main__':
    # Forma mais facil de entender e implementar nos programas
    print(Color.BOLD + Color.CYAN + '\nHello World !\n' + Color.END)

    # Outra forma
    print('\n\n')
    print('\033[31m'+'Vermelho'+'\033[0;0m')
    print('\033[32m'+'Verde'+'\033[0;0m')
    print('\033[34m'+'Azul'+'\033[0;0m')
    print('\033[36m'+'Ciano'+'\033[0;0m')
    print('\033[35m'+'Magenta'+'\033[0;0m')
    print('\033[33m'+'Amarelo'+'\033[0;0m')
    print('\033[30m'+'Preto'+'\033[0;0m')
    print('\033[37m'+'Branco'+'\033[0;0m')
    print('\033[0;0m'+'Original'+'\033[0;0m')
    print('\033[1m'+'Negrito'+'\033[0;0m')
    print('\033[2m'+'Reverso'+'\033[0;0m')
    print('\033[40m'+'Fundo Preto'+'\033[0;0m')
    print('\033[41m'+'Fundo Vermelho'+'\033[0;0m')
    print('\033[42m'+'Fundo Verde'+'\033[0;0m')
    print('\033[43m'+'Fundo Amarelo'+'\033[0;0m')
    print('\033[44m'+'Fundo Azul'+'\033[0;0m')
    print('\033[45m'+'Fundo Magenta'+'\033[0;0m')
    print('\033[46m'+'Fundo Ciano'+'\033[0;0m')
    print('\033[47m'+'Fundo Branco'+'\033[0;0m')
    print('\n\n')