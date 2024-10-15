from math import inf

class HeapMinima:
    def __init__(self, listaElementos=None):
        if listaElementos is None:
            listaElementos = []
        self.tamanhoHeap: int = len(listaElementos)
        self.vetorElementos: list[int|float] = listaElementos

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

        if filhoEsquerdo < self.tamanhoHeap and self.vetorElementos[filhoEsquerdo] < self.vetorElementos[indice]:
            menorElemento = filhoEsquerdo

        if filhoDireito < self.tamanhoHeap and self.vetorElementos[filhoDireito] < self.vetorElementos[menorElemento]:
            menorElemento = filhoDireito

        if menorElemento != indice:
            temp: int = self.vetorElementos[indice]
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
            temp: int = self.vetorElementos[0]
            self.vetorElementos[0] = self.vetorElementos[i]
            self.vetorElementos[i] = temp
            self.tamanhoHeap -= 1
            self.minHeapfy(0)
            

    def inserirElemento(self, elemento: int) -> None:
        self.tamanhoHeap += 1
        self.vetorElementos.append(-1)
        self.vetorElementos[self.tamanhoHeap - 1] = inf
        self.diminuirValorElemento(self.tamanhoHeap - 1, elemento)

    def obterElementoMinimo(self) -> int:
        return self.vetorElementos[0]

    def removerElementoMinimo(self) -> int:
        if self.tamanhoHeap < 1:
            print("Heap não possui elementos")
            return -1

        elementoMinimo: int = self.vetorElementos[0]
        self.vetorElementos[0] = self.vetorElementos[self.tamanhoHeap - 1]
        self.tamanhoHeap -= 1

        self.minHeapfy(0)
        return elementoMinimo

    def __len__(self):
        return self.tamanhoHeap


    def diminuirValorElemento(self, tamanhoHeap: int, elemento: int) -> None:
        if elemento > self.vetorElementos[tamanhoHeap]:
            print("Erro")
            return

        self.vetorElementos[tamanhoHeap] = elemento
        while tamanhoHeap > 0 and self.vetorElementos[self.getPai(tamanhoHeap)] > self.vetorElementos[tamanhoHeap]:
            temp: int = self.vetorElementos[tamanhoHeap]
            self.vetorElementos[tamanhoHeap] = self.vetorElementos[self.getPai(tamanhoHeap)]
            self.vetorElementos[self.getPai(tamanhoHeap)] = temp
            tamanhoHeap = self.getPai(tamanhoHeap)
    

    def __str__(self) -> str:
        return str(self.vetorElementos)
