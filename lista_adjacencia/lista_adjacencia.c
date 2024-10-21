#include <stdlib.h>
#include <stdio.h>
#include "lista_encadeada.c"

/*
 * OBSERVAÇÃO: Na função menu(), chamo a função cls(). Ela só é válida para Windows.
 *             Deve-se modificá-la, caso o programa seja executado em outro sistema 
 *             operacional.
 */

typedef struct elementoListaAdj {
    int rotulo;
    No *listaEncadeada;
} ElementoListaAdj;

void estouroDeMemoria();
int inicializaListasEncadeadas(ElementoListaAdj**, int);
int adicionaAresta(ElementoListaAdj**, int, int, int);
void menu(ElementoListaAdj**, int);
void lerArestas(ElementoListaAdj**, int);
void imprimirListaAdjacencia(ElementoListaAdj**, int);
void imprimirListaAdjVertice(ElementoListaAdj**, int);
ElementoListaAdj *buscaElementoListaAdj(ElementoListaAdj**, int, int);

void lerArestas(ElementoListaAdj **listaAdj, int tamanhoLista) {
    ElementoListaAdj *lista = *listaAdj;

    int qtdArestas, verticeInicial, verticeFinal;

    printf("Insira a quantidade de arestas que voce deseja adicionar: ");
    scanf("%d", &qtdArestas);

    if (qtdArestas < 0) {
        printf("Quantidade invalida\n");
        return;
    }

    printf("Insira os valores dos vertices iniciais e finais separados por espacos (ex.: 1 2)\n");
    for (int i = 0; i < qtdArestas; ++i) {
        scanf("%d %d", &verticeInicial, &verticeFinal);

        adicionaAresta(listaAdj, verticeInicial, verticeFinal, tamanhoLista);
    }

}

void imprimirListaAdjacencia(ElementoListaAdj **listaAdj, int tamanhoLista) {
    ElementoListaAdj *lista = *listaAdj;

    ElementoListaAdj elementoTemp;

    for (int i = 0; i < tamanhoLista; ++i) {
        elementoTemp = lista[i];

        printf("%d -> ", elementoTemp.rotulo);
        imprimeListaEncadeada(&(elementoTemp.listaEncadeada));
    }

}

void imprimirListaAdjVertice(ElementoListaAdj **listaAdj, int qtdVertices) {
    ElementoListaAdj *lista = *listaAdj;

    int vertice;

    printf("Insira o rotulo do vertice: ");
    scanf("%d", &vertice);

    ElementoListaAdj *elementoTemp = buscaElementoListaAdj(listaAdj, vertice, qtdVertices);

    if (elementoTemp == NULL) {
        printf("Rotulo invalido\n");
        return;
    }

    if (elementoTemp->listaEncadeada == NULL) {
        printf("Vertice nao possui vertices adjacentes\n");
        return;
    }
    imprimeListaEncadeada(&(elementoTemp->listaEncadeada));

}


ElementoListaAdj *criarListaAdj(int tamanhoLista) {
    ElementoListaAdj *listaAdjacencia = malloc(sizeof(ElementoListaAdj) * tamanhoLista);

    return listaAdjacencia;
}

int inicializaListasEncadeadas(ElementoListaAdj **listaAdj, int tamanhoLista) {
    ElementoListaAdj *vetor = *listaAdj;
    ElementoListaAdj *elem;
    int rotulo;

    for (int i = 0; i < tamanhoLista; ++i) {
        printf("\nDigite o rotulo do %do vertice: ", i+1);
        scanf("%d", &rotulo);

        elem = malloc(sizeof(ElementoListaAdj));

        if (elem == NULL) {
            estouroDeMemoria();
        }

        elem->rotulo = rotulo;
        elem->listaEncadeada = NULL;

        vetor[i] = *elem;

    }

    return 1;
}

int adicionaAresta(ElementoListaAdj **listaAdj, int verticeInicial, int verticeFinal, int tamanhoLista) {
    ElementoListaAdj *elementoTemp1 = buscaElementoListaAdj(listaAdj, verticeInicial, tamanhoLista);
    ElementoListaAdj *elementoTemp2 = buscaElementoListaAdj(listaAdj, verticeFinal, tamanhoLista);

    if (elementoTemp1 == NULL || elementoTemp2 == NULL) {
        printf("Nao existe(m) vertice(s) com esse(s) rotulo(s)\n");
        return 0;
    }

    if (elementoTemp1->listaEncadeada == NULL) {
        No *noTemp = malloc(sizeof(No));

        if (noTemp == NULL) {
            estouroDeMemoria();
        }

        noTemp->rotulo = verticeFinal;
        noTemp->proxNo = NULL;
        elementoTemp1->listaEncadeada = noTemp;
    }
    else {
        inserirElemento(verticeFinal, &(elementoTemp1->listaEncadeada));
    }

    if (elementoTemp2->listaEncadeada == NULL) {
        No *noTemp = malloc(sizeof(No));

        if (noTemp == NULL) {
            estouroDeMemoria();
        }

        noTemp->rotulo = verticeFinal;
        noTemp->proxNo = NULL;
        elementoTemp2->listaEncadeada = noTemp;
    }
    else {
        inserirElemento(verticeFinal, &(elementoTemp2->listaEncadeada));
    }

    return 1;

}

ElementoListaAdj *buscaElementoListaAdj(ElementoListaAdj **listaAdj, int vertice, int tamanhoLista) {
    ElementoListaAdj *lista = *listaAdj;
    ElementoListaAdj* elementoTemp;

    for (int i = 0; i < tamanhoLista; ++i) {
        elementoTemp = &lista[i];
        
        if (elementoTemp->rotulo == vertice) {
            return elementoTemp;
        }
    }

    return NULL;
}

void estouroDeMemoria() {
     printf("Limide de memoria excedido\n");
     exit(1);
}

void menu(ElementoListaAdj **listaAdj, int qtdVertices) {
    int opcao = 0;
    char lixo1, lixo2;
    
    do {
        system("cls");
        printf("\n\nMENU\n");
        printf("0 - encerrar\n");
        printf("1 - ler n arestas\n");
        printf("2 - exibir lista de adjacencia do vertice v\n");
        printf("3 - imprimir lista de adjacencia\n");

        printf("Digite uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 0:
                exit(0);
            case 1:
                lerArestas(listaAdj, qtdVertices);
                break;
            case 2:
                imprimirListaAdjVertice(listaAdj, qtdVertices);
                break;
            case 3:
                imprimirListaAdjacencia(listaAdj, qtdVertices);
                break;
            default:
                printf("Opcao invalida\n");
        }

        printf("Tecle ENTER para continuar...");
        scanf("%c%c", &lixo1, &lixo2);
    } while (opcao != 0);
}

int main() {

    int qtdVertices;

    printf("Insira a quantidade de vertices do grafo: ");
    scanf("%d", &qtdVertices);

    
    ElementoListaAdj *listaAdjacencia = criarListaAdj(qtdVertices);

    if (listaAdjacencia == NULL) {
        estouroDeMemoria();
        return 1;
    }

    inicializaListasEncadeadas(&listaAdjacencia, qtdVertices);

    menu(&listaAdjacencia, qtdVertices);


    return 0;
}
