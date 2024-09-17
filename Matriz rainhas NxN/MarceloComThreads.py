import random
from threading import Thread
import time
import timeit


def criaMatriz(tamanho):
    matriz = []
    for x in range(tamanho):
        linha = []
        for y in range(tamanho):
            linha.append(0)
        matriz.append(linha)
    return matriz

def imprimeMatriz(matriz,tamanho):
    for i in range(tamanho):
        print(matriz[i])

def verificaDisp(lin, col, linOcupada, colOcupada):
    for i in range(len(linOcupada)):
        if abs(lin - linOcupada[i]) == abs(col - colOcupada[i]):
            return False
    return True

def posicionaRainha(matriz, linOcupada, colOcupada, erro,tamanho):
    tentativas = 0
    while tentativas < tamanho * 10:
        lin = len(linOcupada)
        col = random.choice([num for num in range(0, tamanho) if num not in colOcupada])
        if verificaDisp(lin, col, linOcupada, colOcupada):
            linOcupada.append(lin)
            colOcupada.append(col)
            matriz[lin][col] = 1
            erro = False
            break
        tentativas+=1
    if tentativas == tamanho * 10:
        erro = True
    return erro

def threadRainha(numRandom,tamanho):
    erro = True
    while erro:
        erro = False
        matriz = criaMatriz(tamanho)
        linOcupada = []
        linOcupada.append(0)
        colOcupada = []
        colOcupada.append(numRandom)
        matriz[linOcupada[0]][colOcupada[0]] = 1
        for i in range (1, tamanho):
            erro = posicionaRainha(matriz, linOcupada, colOcupada,erro,tamanho)
            if erro:
                break
            
    print("")
    imprimeMatriz(matriz,tamanho)

def main():
    tamanho = int(input("Digite o tamanho da matriz de NxN rainhas: "))
    vet = []
    for i in range(tamanho):
        vet.append(i)
    
    print(vet)
    a = random.choice(vet)
    vet.remove(a)
    b = random.choice(vet)
    vet.remove(b)
    
    thread1 = Thread(target=threadRainha, args=[a,tamanho])
    thread2 = Thread(target=threadRainha, args=[b,tamanho])
    thread1.start()


    thread1.join()
  
  

main()