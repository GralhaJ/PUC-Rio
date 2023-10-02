/*
33B
João Gabriel Gralha Quirino de Souza
2310284
*/

#include <stdio.h>
#include <stdlib.h>
#include "matriz.h"

int main()
{
    double constante, escalar;
    double **matriz, **matrizFinal, **matrizIdentidade;
    int linhas, colunas, identidade;

    printf("Insira o numero de linhas: ");
    scanf("%d", &linhas);
    printf("Insira o número de colunas: ");
    scanf("%d", &colunas);
    printf("Insira o valor da constante: ");
    scanf("%lf", &constante);

    Matriz(linhas, colunas, constante, &matriz);
    printf("Matriz %dx%d com elementos iguais a %.1lf:\n", linhas, colunas, constante);
    ImprimeMatriz(linhas, colunas, matriz);
    printf("\n");

    SomaMatrizes(linhas, colunas, &matriz, &matriz, &matrizFinal);
    printf("Matriz que eh resultado da soma de duas matrizes iguais as anteriores:\n");
    ImprimeMatriz(linhas, colunas, matrizFinal);
    printf("\n");

    printf("Informe o escalar para realizar a multiplicacao: ");
    scanf("%lf", &escalar);
    MultiplicacaoPorEscalar(linhas, colunas, escalar, &matrizFinal);
    printf("Matriz que eh o resultado da ultima matriz com seus elementos multiplicados por 3:\n");
    ImprimeMatriz(linhas, colunas, matrizFinal);
    printf("%\n");

    for (int i = 0; i < linhas; i++)
    {
        free(matrizFinal[i]);
        free(matriz[i]);
    }
    free(matrizFinal);
    free(matriz);

    printf("Como a matriz identidade eh quadrada, indique a sua dimensao: ");
    scanf("%d", &identidade);
    MatrizIdentidade(identidade, identidade, &matrizIdentidade);
    printf("Matriz identidade de dimensao %dx%d:\n", identidade, identidade);
    ImprimeMatriz(identidade, identidade, matrizIdentidade);

    for (int i = 0; i < linhas; i++)
    {
        free(matrizIdentidade[i]);
    }
    free(matrizIdentidade);
    
    return 0;
}