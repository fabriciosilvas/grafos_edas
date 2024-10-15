from heap_minima_par import HeapMinimaPar

def gerarCodigoPruffer(matrizAdjacencia: list[list[int]]) -> list[int]:
    grauVertices: list[list[int]] = [[linha + 1, sum(matrizAdjacencia[linha])] for linha in range(len(matrizAdjacencia))]

    heap = HeapMinimaPar(grauVertices)

    codigoPruffer: list[int] = [0] * (len(matrizAdjacencia) - 2)

    for i in range(len(matrizAdjacencia) - 2):
        elementoMinimo: list[int] = heap.removerElementoMinimo()


        j: int = elementoMinimo[0] - 1

        k: int = 0

        while not matrizAdjacencia[j][k]:
            k += 1

        codigoPruffer[i] = k + 1
        matrizAdjacencia[k][j] = 0
        heap.decrementarGrauVertice(k + 1)

    return codigoPruffer

if __name__ == '__main__':
    qtdVertices: int = int(input("Digite a quantidade de vértices: "))

    listaAdjacencia: list[list[int]] = [[0]*qtdVertices for _ in range(qtdVertices)]

    print("\nTipos de grafos\n[1] não-direcionado\n[2] direcionado")
    tipoGrafo: int = int(input("Digite o tipo do grafo: "))

    #qtdArestas: int = int(input("\nDigite a quantidade de arestas: "))

    print("\nDigite as arestas no formato 'ai aj', sem as aspas e '-1 -1' para finalizar a leitura")

    if tipoGrafo == 1:
        #for i in range(qtdArestas):
        ai, aj = map(int, input().split())
        while ai != -1 and aj != -1:
            listaAdjacencia[ai - 1][aj - 1] = 1
            listaAdjacencia[aj - 1][ai - 1] = 1
            ai, aj = map(int, input().split())
    elif tipoGrafo == 2:
        #for  i in range(qtdArestas):
        ai, aj = map(int, input().split())
        while ai != -1 and aj != -1:
            ai, aj = map(int, input().split())
            listaAdjacencia[ai - 1][aj - 1] = 1

    print(f"Código de Pruffer do grafo: {gerarCodigoPruffer(listaAdjacencia)}")