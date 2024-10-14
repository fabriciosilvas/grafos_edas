class HeapMinima:
    def __init__(self, listaElementos:list[int]=[]):
        self.qtdElementos: int = len(listaElementos)
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

        if filhoEsquerdo < self.qtdElementos and self.vetorElementos[filhoEsquerdo] < self.vetorElementos[indice]:
            menorElemento = filhoEsquerdo

        if filhoDireito < self.qtdElementos and self.vetorElementos[filhoDireito] < self.vetorElementos[menorElemento]:
            menorElemento = filhoDireito

        if menorElemento != indice:
            temp: int = self.vetorElementos[indice]
            self.vetorElementos[indice] = self.vetorElementos[menorElemento]
            self.vetorElementos[menorElemento] = temp

            self.minHeapfy(menorElemento)

    def construirHeapMinima(self) -> None:
        tamanhoHeap: int = len(self.vetorElementos)
        for i in range((tamanhoHeap - 2) // 2, -1, -1):
            self.minHeapfy(i)

    def heapSort(self):
        pass

    def inserirElemento(self):
        pass

    def obterElementoMinimo(self):
        pass

    def removerElementoMinimo(self):
        pass

    def diminuirValorElemento(self):
        pass

    def __str__(self) -> str:
        return str(self.vetorElementos)

if __name__ == '__main__':
    lista = [4,1,3,2,16,9,10,14,8,7]
    heapTeste = HeapMinima(lista)
    print(heapTeste)
    heapTeste.construirHeapMinima()
    print(heapTeste)