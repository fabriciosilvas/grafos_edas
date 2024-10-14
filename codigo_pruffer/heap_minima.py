class HeapMinima:
    def __init__(self, listaElementos:list[int]=[]):
        self.qtdElementos: int = len(listaElementos)
        self.tamanhoHeap: int = self.qtdElementos
        self.vetorElementos: list[int] = listaElementos

    def getPai(self, indice: int) -> int:
        return (indice - 1) // 2

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
        self.tamanhoHeap = self.qtdElementos
        tamanhoHeap: int = len(self.vetorElementos)
        for i in range((tamanhoHeap - 2) // 2, -1, -1):
            self.minHeapfy(i)

    def heapSort(self) -> None:
        tamanhoHeap: int = len(self.vetorElementos)
        for i in range(tamanhoHep - 1, 0, -1):
            temp: int = self.vetorElementos[0]
            self.vetorElementos[0] = self.vetorElementos[i]
            self.vetorElementos[i] = temp
            self.tamanhoHeap -= 1
            self.minHeapfy(0)
            

    def inserirElemento(self, elemento: indice) -> None:
        self.tamanhoHeap += 1
        self.vetoElementos[self.tamahoHeap - 1] = -inf
        self.diminuirValorElemento(self.tamahoHeap, elemento)

    def obterElementoMinimo(self) -> int:
        return self.vetorElementos[0]

    def removerElementoMinimo(self):
        pass

    def diminuirValorElemento(self, tamanhoHeap: int, elemento: int) -> None:
        if elemento < self.vetorElementos[tamanhoHeap - 1]:
            print("Erro")
            return
        self.vetorElementos[tamanhoHeap - 1] = elemento
        while tamahoHeap > 0 and self.vetorElementos[self.getPai(tamanhoHeap-1)] < self.vetorElementos[tamanhoHeap - 1]:
            temp: int = self.vetorElementos[tamanhoHeap - 1]
            self.vetorElementos[tamanhoHeap - 1] = self.vetorElementos[self.getPai(tamanhoHeap - 1)]
            self.vetorElementos[self.getPai(tamanhoHeap - 1)] = temp
            tamanhoHeap = self.getPai(tamanhoHeap - 1)
    

    def __str__(self) -> str:
        return str(self.vetorElementos)

if __name__ == '__main__':
    lista = [4,1,3,2,16,9,10,14,8,7]
    heapTeste = HeapMinima(lista)
    print(heapTeste)
    heapTeste.construirHeapMinima()
    print(heapTeste)
