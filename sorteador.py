import funcoes as f
from random import choice
from tkinter import *

def main():
    naoSorteados = []
    jaSorteados = []

    if f.existeArquivo("bd/nao_sorteados.txt"):
        # Recuperação dos arquivos com os nomes NÃO sorteados e JÁ sorteados, caso o arquivo exista
        # Os nome recuperados são inseridos em listas
        print("\nRecuperando Nomes Nao Sorteados...")
        f.recuperarArquivo(naoSorteados, "bd/nao_sorteados.txt")
        if f.existeArquivo("bd/ja_sorteados.txt"):
            print("Recuperando Nomes Ja Sorteados...")
            f.recuperarArquivo(jaSorteados, "bd/ja_sorteados.txt")

        if naoSorteados[0] == "":
            print("\nTodos os nomes já foram sorteados!\nResetando lista...")
            naoSorteados = jaSorteados
            jaSorteados = []

        print("\nAINDA NAO FORAM SORTEADOS:")
        f.mostrarNomes(naoSorteados)

        # Sorteio do nome
        nomeSorteado = choice(naoSorteados)
        print(f"\nQuem limpa a cafeteira hoje e: {nomeSorteado.upper()}")
        texto_saida["text"] = nomeSorteado.upper() # saída na interface

        # Tirando o nome de uma lista e inserindo na outra
        naoSorteados.pop(naoSorteados.index(nomeSorteado))
        jaSorteados.append(nomeSorteado)

        print("\nJA FORAM SORTEADOS:")
        f.mostrarNomes(jaSorteados)

        # Gravação dos nomes nos arquivos
        print("\nGravando Nomes Nao Sorteados...")
        f.gravarArquivo(jaSorteados, "bd/ja_sorteados.txt")
        print("Gravando Nomes Ja Sorteados...")
        f.gravarArquivo(naoSorteados, "bd/nao_sorteados.txt") 

    else:
        print("\nArquivo com os nomes nao encontrado! :(\n")

# main()

# Cria a janela
janela = Tk()
janela.title("Sorteador")
# janela.geometry("400x400") // Dimenção da janela

# primeiro parâmetro: qual janela vou usar
texto_sorteio = Label(janela, text="Quem limpa a cafeteira hoje é:")
texto_sorteio.grid(column=0, row=0, padx=100, pady=10)

texto_saida = Label(janela, text="")
texto_saida.grid(column=0, row=1)

temp = 0

# command refere-se à função que será executada
botao = Button(janela, text="Sortear", command=main)
botao.grid(column=0, row=2, padx=10, pady=20)

# mantem a janela aberta
janela.mainloop()