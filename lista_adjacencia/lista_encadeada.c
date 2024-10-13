#include <stdlib.h>
#include <stdio.h>

typedef struct no {
    int rotulo;
    struct no *proxNo;
} No;

No *inserirElemento(int, No**);
No *removerElemento(int, No**);
int tamanhoLista(No**);
No *buscarElemento(int, No**);
void imprimeListaEncadeada(No**);


No *inserirElemento(int elemento, No **lista) {
    No *cabeca = *lista;
    No *temp = *lista;
    No *novoElemento = malloc(sizeof(No));

    if (novoElemento == NULL) {
        return NULL;
    }

    novoElemento->rotulo = elemento;
    novoElemento->proxNo = NULL;

    while (temp->proxNo != NULL) {
        temp = temp->proxNo;
    }

    temp->proxNo = novoElemento;

    return cabeca;
}

No *removerElemento(int elemento, No **lista) {
    No *cabeca = *lista;
    No *noAtual = *lista;
    No *noAnterior = NULL;

    if (noAtual == NULL) {
        return NULL;
    }

    if (noAtual->rotulo == elemento) {
        cabeca = noAtual->proxNo;
        noAtual->proxNo = NULL;
        free(noAtual);

        return cabeca;
    }
    

    while (noAtual != NULL && noAtual->rotulo != elemento) {
        noAnterior = noAtual;
        noAtual = noAtual->proxNo;
    }

    if (noAtual == NULL) {
        return cabeca;
    }

    if (noAtual->proxNo == NULL) {
        noAnterior->proxNo = NULL;
        free(noAtual);

        return cabeca;
    }

    noAnterior->proxNo = noAtual->proxNo;
    noAtual->proxNo = NULL;
    free(noAtual);

    return cabeca;
}

int tamanhoLista(No **lista) {
    int qtd = 0;

    No *noAtual = *lista;

    if (noAtual == NULL) {
        return 0;
    }

    while (noAtual != NULL) {
        ++qtd;
        noAtual = noAtual->proxNo;
    }

    return qtd;
}

No *buscarElemento(int elemento, No **lista) {
    No *noAtual = *lista;

    if (noAtual == NULL) {
        return NULL;
    }

    while (noAtual != NULL && noAtual->rotulo != elemento) {
        noAtual = noAtual->proxNo;
    }

    return noAtual;
}

void imprimeListaEncadeada(No **lista) {
     No *noAtual = *lista;

    if (noAtual == NULL) {
        printf("Lista vazia\n");
        return;
    }

    printf("[");

    while (noAtual->proxNo != NULL) {
        printf("%d, ", noAtual->rotulo);
        noAtual = noAtual->proxNo;
    }

    printf("%d]\n", noAtual->rotulo);
}

