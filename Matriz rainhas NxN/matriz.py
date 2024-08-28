#Função responsável por gerar a matriz de um tamanho x

def criaMatriz(tam):
    matriz = []
    for x in range(tam):
        linha = []
        for y in range(tam):
            linha.append(0)
        matriz.append(linha)
    return matriz





def main():
    tamanho = int(input("Digite o tamanho da matriz de NxN rainhas: "))
    matriz = criaMatriz(tamanho)
    print(matriz)


main()