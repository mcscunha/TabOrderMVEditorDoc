#!/Anaconda3/Scripts/tabordereditordoc python
# -*- coding: utf-8 -*-

#title           :principal.py
#description     :Este script serve para pegar, de um XML, todos os elementos configurados em uma lista e trata-los
#author          :MuriloCunha
#date            :20181018
#version         :1.0
#usage           :python principal.py
#notes           :
#python_version  :3.6
#==============================================================================

# TODO Listar todas as linhas possiveis de edicao
# TODO Alterar as linhas escolhidas
# TODO Lancar um "mapa" dos componentes, com KEY e TABINDEX

# Import the modules needed to run the script.
from util import Color as textcolor
from elem_tree_func import ET, encontrar_elemento, listar_linhas


LST_ELEMENTOS = ['CHECKBOX', 'TEXT', 'DATE', 'RADIOBUTTON', 'TEXTAREA', 'RADIOBUTTON']
DEF_ARQ = "XML Teste 2.xml"


def listar_elemento(strNos, lstElemento):
    for elemento in lstElemento:
        linhas = listar_linhas(root, strNos + elemento )
        print(elemento)
        for linha in linhas:
            print('\t', linha.attrib['key'], '\t- ', linha.attrib['tabIndex'])


if __name__ == '__main__':
    print(textcolor.BLUE, 'Usando:', textcolor.BLUE+textcolor.BOLD, 'ElementTree', textcolor.END)

    # Abrindo arquivo XML
    try:
        dom = ET.parse(DEF_ARQ)
        root = dom.getroot()
    except:
        exit("Não foi possível abrir o arquivo: " + DEF_ARQ)

    # Testando algumas propriedades
    print('Pegando as primeiras TAG´s:', [elem.tag for elem in root.iter()][0:11] )
    print('TAG e ATTRIB onde o ponteiro está parado:', root.tag, root.attrib)
    print('Listar tudo com a TAG=CHECKBOX:', [(a.attrib['key'], a.attrib['tabIndex'], a.text) for a in root.iter('CHECKBOX')] )


    listar_elemento('./Page/Row/Column/', LST_ELEMENTOS)
    chaves = ['key', 'tabIndex', 'x', 'y']
    enc_elem = encontrar_elemento(root, ".//*[@key='Metadado_154_17']")
    if enc_elem != []:
        print(enc_elem.get('key'), '\t', enc_elem.get('tabIndex'), '\t', enc_elem.get('x'), '\t', enc_elem.get('y'))
        print([{chave: enc_elem.get(chave)} for chave in chaves])

    # # Outra maneira de procurar os elementos
    # enc_elem = encontrar_elemento(root, './/*' + LST_ELEMENTOS[0] + '')
    # print(len(enc_elem))
    # if enc_elem != []:
    #     for elemento in enc_elem:
    #         print('TAGs:', elemento.get('key'), '\t', elemento.get('tabIndex'))
    #         if (elemento.get('key') != None) and (elemento.get('tabIndex') != None):
    #             print('TAGs:', elemento.attrib['key'], '\t', elemento.attrib['tabIndex'])




    # Parse to find the child nodes list of node 'myNode'
    fwdefs = encontrar_elemento(root, ".//*CHECKBOX") # /[@id='298056']")
    if fwdefs is not None:
        print('Encontrado TAG \t\t:', fwdefs.tag)
        print('Encontrado ATTRIB\t:', fwdefs.attrib)
        print('Encontrado TEXT\t\t:', fwdefs.text)

