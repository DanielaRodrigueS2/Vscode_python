#Função responsável por gerar a matriz de um tamanho x usando listas dentro de listas

def criaMatriz(tam):
    matriz = []
    for x in range(tam):
        linha = []
        for y in range(tam):
            linha.append(0)
        matriz.append(linha)
    return matriz

#função que imprime a matriz linha/linha

def imprimeMatriz(matriz, tam):
    for i in range(tam):
        print(matriz[i])

#função que testa se existem 2 rainhas em uma mesma coluna

def testaColuna(matriz, tam, i, j):
    sum = 0
    for x in range(tam):
        if matriz[x][j] == 1:
            sum += 1

    if sum < 2:
        return True
    else:
        return False
    
#função que testa se existe outra rainha na diagonal direita onde a rainha que foi colocada está

def testaDiagonalD(matriz, tam, i, j):
    sum = 0
    x = i
    y = j

    #testa diagona de cima i+1 j+1
    while(x >= 0 and y>=0):
        x -= 1
        y -=1
        if(matriz[x][y] == 1):
            sum+= 1

    x = i
    y = j

    #testa diagonal de baixo i-1
    while(x < tam and y < tam):
        x += 1
        y +=1
        if(matriz[x][y] == 1):
            sum+= 1

    if sum < 2:
        return True
    else:
        return False


 #função que testa se existe outra rainha na diagonal esquerda onde a rainha que foi colocada está
   
def testaDiagonaE(matriz, tam, i, j):
    sum = 0
    x = i
    y = j

    # testa se existe outra rainha na diagonal esquerda acima i-1 j+1
    while(x>=0 and y < tam):
        x -=1
        y += 1
        if(matriz[x][y] == 1):
            sum+= 1

    x = i
    y = j

    # testa se existe outra rainha na diagonal esquerda abaixo i+1 j-1
    while(x < tam and y >= 0):
        x += 1
        y -= 1
        if(matriz[x][y] == 1):
            sum+= 1
    
    if sum < 2:
        return True
    else:
        return False

def colocaRainha(matriz, tam):
    return
    
    

def main():
    tamanho = int(input("Digite o tamanho da matriz de NxN rainhas: "))
    matriz = criaMatriz(tamanho)
    imprimeMatriz(matriz,tamanho)



main()
