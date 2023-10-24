#include<stdio.h>
#include "funcoes.h"

int obter_codigo()
{
	int codigo;
	printf("Digite seu codigo: ");
	scanf("%d", codigo);
	return codigo;
}

float obter_frete()
{
	float frete;
	printf("Digite o preco inicial do frete: ");
	scanf("%f", frete);
	return frete;
}

int obter_marca()
{
	int marca;
	printf("Digite a marca do ovo (1 - Nestle, 2 - Lacta, 3 - Garoto:");
	scanf("%d", &marca);
	return marca;
}

int obter_tamanho()
{
	int tamanho;
	printf("Digite o tamanho dos ovo: ");
	scanf("%d", &tamanho);
	return tamanho;
}

int obter_quantidade()
{
	int quantidade;
	printf("Digite a quantidade deovos comprados: ");
	scanf("%d", &quantidade);
	return quantidade;
}
float obter_desconto(int* marca, int* tamanho, int* quantidade)
{
	if (*marca == 1)
	{
		if (*quantidade <= 5)
		{
			return 0.1;
		}
		else if(*quantidade <=8)
		{
			return 0.2;
		}
		else
		{
			return 1.0;
		}
	}
	else if (*marca == 2)
	{
		if (*quantidade > 3)
		{
			if (*tamanho >= 21)
			{
				return 0.1;
			}
			else
			{
				return 0.05;
			}
		}
		else if (*quantidade > 8)
		{
			return 1.0;
		}
	}
	else if (*marca == 3)
	{
		if (*quantidade > 8)
		{
			return 1.0;
		}
		else if (*tamanho >= 21)
		{
			return 0.15;
		}
		else
		{
			return 0.07;
		}
	}
}