#include <stdio.h>
#include <stdlib.h>

void Matriz(int linhas, int colunas, double constante, double*** matriz)
{
    *matriz = (double **)malloc(linhas * sizeof(double *));
    for (int i = 0; i < linhas; i++)
    {
        (*matriz)[i] = (double *)malloc(colunas * sizeof(double));
    }
    for (int i = 0; i < linhas; i++)
    {
        for (int j = 0; j < colunas; j++)
        {
            (*matriz)[i][j] = constante;
        }
    }
}

void ImprimeMatriz(int linhas, int colunas, double **matriz)
{
    for (int i = 0; i < linhas; i++)
    {
        printf("|");
        for (int j = 0; j < colunas; j++)
        {
            printf(" %.1lf ", matriz[i][j]);
        }
        printf("|\n");
    }
}

void MatrizIdentidade(int linhas, int colunas, double ***matriz)
{
    *matriz = (double**)malloc(linhas * sizeof(double*));
    for (int i = 0; i < linhas; i++)
    {
        (*matriz)[i] = (double*)malloc(colunas * sizeof(double));
    }
    for (int i = 0; i < linhas; i++)
    {
        for (int j = 0; j < colunas; j++)
        {
            if (i == j)
            {
                (*matriz)[i][j] = 1;
            }
            else
            {
                (*matriz)[i][j] = 0;
            }
        }
    }
}

void SomaMatrizes(int linhas, int colunas, double*** matrizA, double*** matrizB, double*** matrizFinal)
{
    *matrizFinal = (double**)malloc(linhas * sizeof(double*));

    for (int i = 0; i < linhas; i++)
    {
        (*matrizFinal)[i] = (double*)malloc(colunas * sizeof(double));
        for (int j = 0; j < colunas; j++)
        {
            (*matrizFinal)[i][j] = (*matrizA)[i][j] + (*matrizB)[i][j];
        }
    }
}

void MultiplicacaoPorEscalar(int linhas, int colunas, double escalar, double*** matrizMultiplicada) 
{
    for (int i=0; i<linhas; i++)
    {
        for (int j=0; j<colunas; j++)
        {
            (*matrizMultiplicada)[i][j] = (*matrizMultiplicada)[i][j] * escalar;
        }
    }
}