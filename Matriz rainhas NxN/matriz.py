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

def testaColuna(matriz, tam, j):
    sum = 0
    for x in range(tam):
        if matriz[x][j] == 1:
            sum += 1

    if sum == 0:
        return True
    else:
        return False
    
#função que testa se existe outra rainha na diagonal direita onde a rainha que foi colocada está

def testaDiagonalD(matriz, tam, i, j):
    sum = 0
    x = i-1
    y = j-1

    #testa diagona de cima i-1 j-1
    while(x >= 0 and y>=0):
        if(matriz[x][y] == 1):
            sum+= 1
        x -= 1
        y -=1
        

    x = i+1
    y = j+1

    #testa diagonal de baixo i+1 j+1
    while(x < tam and y < tam):
        if(matriz[x][y] == 1):
            sum+= 1
        x += 1
        y +=1

    if sum < 1:
        return True
    else:
        return False


 #função que testa se existe outra rainha na diagonal esquerda onde a rainha que foi colocada está
   
def testaDiagonaE(matriz, tam, i, j):
    sum = 0
    x = i -1
    y = j + 1

    # testa se existe outra rainha na diagonal esquerda acima i-1 j+1
    while(x>=0 and y < tam):
        if(matriz[x][y] == 1):
            sum+= 1
        x -=1
        y += 1
        

    x = i +1
    y = j -1

    # testa se existe outra rainha na diagonal esquerda abaixo i+1 j-1
    while(x < tam and y >= 0):
        if(matriz[x][y] == 1):
            sum+= 1
        x += 1
        y -= 1
        
    
    if sum < 1:
        return True
    else:
        return False
    

# Função que testa todas as posições validas com as funções de teste de condição    
def posicaoValida(matriz, i, j, tam):
    return (testaColuna(matriz,tam, j) and testaDiagonalD(matriz, tam, i, j) and testaDiagonaE(matriz,tam, i, j))


#Função para colocar as rainhas nas posições usando recursividade
def colocaRainha(matriz, tam, i=0):
    if i >= tam:
        return True
    
    for j in range(tam):
        if posicaoValida(matriz,i, j, tam):
            matriz[i][j] = 1
            if colocaRainha(matriz, tam, i+1):
                return True
            matriz[i][j] = 0

    
    
    

def main():
    tamanho = int(input("Digite o tamanho da matriz de NxN rainhas: "))
    matriz = criaMatriz(tamanho)
    colocaRainha(matriz, tamanho)
    imprimeMatriz(matriz,tamanho)

main()
