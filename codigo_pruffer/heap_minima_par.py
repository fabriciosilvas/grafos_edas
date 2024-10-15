from math import inf


class HeapMinimaPar:
    def __init__(self, listaElementos=None):
        if listaElementos is None:
            listaElementos = []
        else:
            self.vetorElementos: list[list[int | float]] = listaElementos
            self.construirHeapMinima()
        self.tamanhoHeap: int = len(listaElementos)


    def getPai(self, indice: int) -> int:
        return max((indice - 1), 0) // 2

    def getFilhoEsquerdo(self, indice: int) -> int:
        return 2 * indice + 1

    def getFilhoDireito(self, indice: int) -> int:
        return 2 * (indice + 1)

    def minHeapfy(self, indice: int) -> None:
        filhoEsquerdo: int = self.getFilhoEsquerdo(indice)
        filhoDireito: int = self.getFilhoDireito(indice)
        menorElemento: int = indice

        if filhoEsquerdo < self.tamanhoHeap and self.compara(filhoEsquerdo, indice):
            menorElemento = filhoEsquerdo

        if filhoDireito < self.tamanhoHeap and self.compara(filhoDireito, menorElemento):
            menorElemento = filhoDireito

        if menorElemento != indice:
            temp: list[int | float] = self.vetorElementos[indice]
            self.vetorElementos[indice] = self.vetorElementos[menorElemento]
            self.vetorElementos[menorElemento] = temp

            self.minHeapfy(menorElemento)

    def construirHeapMinima(self) -> None:
        self.tamanhoHeap = len(self.vetorElementos)
        tamanhoHeap: int = len(self.vetorElementos)
        for i in range((tamanhoHeap - 2) // 2, -1, -1):
            self.minHeapfy(i)

    def heapSort(self) -> None:
        self.construirHeapMinima()
        tamanhoHeap: int = len(self.vetorElementos)
        for i in range(tamanhoHeap - 1, 0, -1):
            temp: list[int | float] = self.vetorElementos[0]
            self.vetorElementos[0] = self.vetorElementos[i]
            self.vetorElementos[i] = temp
            self.tamanhoHeap -= 1
            self.minHeapfy(0)

    def inserirElemento(self, elemento: list[int | float]) -> None:
        self.tamanhoHeap += 1
        self.vetorElementos.append(list())
        self.vetorElementos[self.tamanhoHeap - 1] = [inf, inf]
        self.diminuirValorElemento(self.tamanhoHeap - 1, elemento)

    def obterElementoMinimo(self) -> list[int | float]:
        return self.vetorElementos[0]

    def removerElementoMinimo(self) -> list[int | float]:
        if self.tamanhoHeap < 1:
            print("Heap não possui elementos")
            return []

        elementoMinimo: list[int | float] = self.vetorElementos[0]
        self.vetorElementos[0] = self.vetorElementos[self.tamanhoHeap - 1]
        self.tamanhoHeap -= 1

        self.minHeapfy(0)
        return elementoMinimo

    def __len__(self):
        return self.tamanhoHeap

    def diminuirValorElemento(self, tamanhoHeap: int, elemento: list[int | float]) -> None:
        if elemento[1] > self.vetorElementos[tamanhoHeap][1]:
            print("Erro")
            return

        self.vetorElementos[tamanhoHeap] = elemento
        while tamanhoHeap > 0 and self.compara(tamanhoHeap, self.getPai(tamanhoHeap)):
            temp: list[int | float] = self.vetorElementos[tamanhoHeap]
            self.vetorElementos[tamanhoHeap] = self.vetorElementos[self.getPai(tamanhoHeap)]
            self.vetorElementos[self.getPai(tamanhoHeap)] = temp
            tamanhoHeap = self.getPai(tamanhoHeap)

    def decrementarGrauVertice(self, rotulo: int) -> None:
        i: int = 0

        while (i < self.tamanhoHeap) and (self.vetorElementos[i][0] != rotulo):
            i += 1

        if i >= self.tamanhoHeap:
            print("Erro g")
            return

        self.diminuirValorElemento(i, [self.vetorElementos[i][0], self.vetorElementos[i][1] - 1])


    def __str__(self) -> str:
        return str(self.vetorElementos)

    def compara(self, posicao1: int, posicao2: int) -> bool:
        if (self.vetorElementos[posicao1][1] < self.vetorElementos[posicao2][1] or
             (self.vetorElementos[posicao1][1] == self.vetorElementos[posicao2][1] and
              self.vetorElementos[posicao1][0] < self.vetorElementos[posicao2][0])
        ):
            return True

        return False


if __name__ == "__main__":
    heap = HeapMinimaPar([[3,2], [1,4], [5,1], [2,1]])

    for i in range(4):
        print(heap.removerElementoMinimo())

    heap = HeapMinimaPar([[3, 2], [1, 4], [5, 1], [2, 1]])
    heap.decrementarGrauVertice(1)
    print("#"*20)
    for i in range(4):
        print(heap.removerElementoMinimo())