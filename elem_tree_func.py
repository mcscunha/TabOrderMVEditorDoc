try:
    import cElementTree as ET
except ImportError:
    try:
        # Python 2.5 need to import a different module
        import xml.etree.cElementTree as ET
    except ImportError:
        exit("Biblioteca cElementTree não encontrada para importar")


def encontrar_elemento(tree, node):
    found = tree.find(node)
    if found == None:
        print("Nenhum [ %s ] no arquivo" % node)
        found = []
    return found

def listar_linhas(tree, marca):
    itens = tree.findall(marca)
    if itens == None:
        print('Marca não encontrada')
        itens = []
    return itens