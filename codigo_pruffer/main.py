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



def lerDadosCoodigoPruffer() -> None:
    qtdVertices: int = int(input("Digite a quantidade de vértices: "))

    listaAdjacencia: list[list[int]] = [[0] * qtdVertices for _ in range(qtdVertices)]

    print("\nTipos de grafos\n[1] não-direcionado\n[2] direcionado")
    tipoGrafo: int = int(input("Digite o tipo do grafo: "))

    # qtdArestas: int = int(input("\nDigite a quantidade de arestas: "))

    print("\nDigite as arestas no formato 'ai aj', sem as aspas e '-1 -1' para finalizar a leitura")

    if tipoGrafo == 1:
        # for i in range(qtdArestas):
        ai, aj = map(int, input().split())
        while ai != -1 and aj != -1:
            listaAdjacencia[ai - 1][aj - 1] = 1
            listaAdjacencia[aj - 1][ai - 1] = 1
            ai, aj = map(int, input().split())
    elif tipoGrafo == 2:
        # for  i in range(qtdArestas):
        ai, aj = map(int, input().split())
        while ai != -1 and aj != -1:
            ai, aj = map(int, input().split())
            listaAdjacencia[ai - 1][aj - 1] = 1

    print(f"Código de Pruffer do grafo: {gerarCodigoPruffer(listaAdjacencia)}")


def gerarGrafoDeCodigoPruffer() -> None:
    codigoPruffer: list[int] = [int(i) for i in input("Digite os valores separados por espaço: \n").split()]

    qtdVertices = len(codigoPruffer) + 2
    matrizAdjacencia: list[list[int]] = [[0] * qtdVertices for _ in range(qtdVertices)]
    vetorGraus: list[list[int]] = [[i + 1, 0] for i in range(qtdVertices)]

    for elemento in codigoPruffer:
        vetorGraus[elemento - 1][1] += 1

    for i in range(qtdVertices):
        vetorGraus[i] = vetorGraus[i] or 1

    heap = HeapMinimaPar(vetorGraus)

    for i in range(len(codigoPruffer)):
        elementoMinimo: list[int] = heap.removerElementoMinimo()
        matrizAdjacencia[codigoPruffer[i] - 1][elementoMinimo[0] - 1] = 1
        matrizAdjacencia[elementoMinimo[0] - 1][codigoPruffer[i] - 1] = 1

        heap.decrementarGrauVertice(codigoPruffer[i])

    elementoMinimo1: list[int] = heap.removerElementoMinimo()
    elementoMinimo2: list[int] = heap.removerElementoMinimo()

    matrizAdjacencia[elementoMinimo1[0] - 1][elementoMinimo2[0] - 1] = 1
    matrizAdjacencia[elementoMinimo2[0] - 1][elementoMinimo1[0] - 1] = 1

    for i in range(qtdVertices):
        for j in range(qtdVertices):
            if matrizAdjacencia[i][j] == 1:
                print(f"({i+1}, {j+1})")



if __name__ == '__main__':
    print("Operações disponíveis: \n[1] Gerar Código de Pruffer\n[2] Gerar grafo a partir de Codigo de Pruffer")
    operacao: int = int(input("Digite a operação que deseja realizar: "))

    if operacao == 1:
        lerDadosCoodigoPruffer()
    if operacao == 2:
        gerarGrafoDeCodigoPruffer()