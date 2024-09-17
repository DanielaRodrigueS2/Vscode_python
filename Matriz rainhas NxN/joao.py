import threading

# Função responsável por gerar a matriz de um tamanho x usando listas dentro de listas
def criaMatriz(tam):
    matriz = []
    for x in range(tam):
        linha = []
        for y in range(tam):
            linha.append(0)
        matriz.append(linha)
    return matriz

# Função que imprime a matriz linha por linha
def imprimeMatriz(matriz, tam):
    for i in range(tam):
        print(matriz[i])


def olha_coluna(tabuleiro, linha, coluna, n):
    for i in range(linha):
        if tabuleiro[i][coluna] == 1:
            return False
        
def olha_diagonal_sup_esq(tabuleiro, linha, coluna, n):
    for i, j in zip(range(linha, -1, -1), range(coluna, -1, -1)):
        if tabuleiro[i][j] == 1:
            return False
        
def olha_diagonal_sup_dir(tabuleiro, linha, coluna, n):
    for i, j in zip(range(linha, -1, -1), range(coluna, n)):
        if tabuleiro[i][j] == 1:
            return False
        

# Função que verifica se é seguro colocar uma rainha na posição (linha, coluna)
def esta_seguro(tabuleiro, linha, coluna, n):
    # Verifica se há alguma rainha na mesma coluna
    threadCol = threading.Thread(target=olha_coluna, args=[tabuleiro, linha, coluna, n])
    threadDiagEsq = threading.Thread(target=olha_diagonal_sup_esq, args=[tabuleiro, linha, coluna, n])
    threadDiagDir = threading.Thread(target=olha_diagonal_sup_dir, args=[tabuleiro, linha, coluna, n])
    threadCol.start()
    threadDiagDir.start()
    threadDiagEsq.start()

    if(threadCol and threadDiagDir and threadDiagEsq):
        return True
    else:
        return False

# Função recursiva para resolver o problema de N rainhas
def resolve_n_rainhas(tabuleiro, linha, n):
    if linha >= n:
        return True

    for i in range(n):
        if esta_seguro(tabuleiro, linha, i, n):
            tabuleiro[linha][i] = 1
            if resolve_n_rainhas(tabuleiro, linha + 1, n):
                return True
            tabuleiro[linha][i] = 0  # backtracking

    return False

# Função principal que executa o programa
def main():
    n = int(input("Digite o tamanho do tabuleiro (n x n): "))# Tamanho do tabuleiro NxN
    tabuleiro = criaMatriz(n)

    # Solicita ao usuário para escolher a coluna da primeira rainha na linha 1
    coluna = int(input(f"Escolha a coluna (0 a {n-1}) para a primeira rainha na linha 1: "))

    # Coloca a primeira rainha na posição escolhida
    tabuleiro[0][coluna] = 1

    # Resolve o problema para as rainhas restantes
    if resolve_n_rainhas(tabuleiro, 1, n):
        print("Solução encontrada:")
        imprimeMatriz(tabuleiro, n)
    else:
        print("Nenhuma solução existe.")

main()