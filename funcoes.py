def existeArquivo(arq):
    import os
    if os.path.exists(arq):
        return True
    else:
        return False

def recuperarArquivo(lista, arquivo):
    arq = open(arquivo,"r")
    linha = arq.readline()

    adicionarValor(linha, lista)

    for linha in arq:
        adicionarValor(linha, lista)
    arq.close()

def adicionarValor(valor, lista):
    if "\n" in valor: 
        lista.append(valor[:-1])
    else:
        lista.append(valor)


def gravarArquivo(lista, arquivo):
    arq = open(arquivo,"w")
    for nome in lista:
        linha = nome + "\n"
        arq.write(linha)
    arq.close()

def mostrarNomes(lista):
    for item in lista:
        print(item)