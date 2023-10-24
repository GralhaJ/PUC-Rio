#include<stdio.h>
#include "funcoes.h"

int main(void)
{
	float custo_frete = 0.0;
	int clientes = 0;
	int clientes_com_desconto = 0;
	int codigo = 0;

	codigo = obter_codigo();

	while (codigo != 0)
	{
		printf("Cliente %d\n", codigo);

		float frete = obter_frete();
		int marca = obter_marca();
		int tamanho = obter_tamanho();
		int quantidade = obter_quantidade();

		float desconto = obter_desconto(&marca, &tamanho, &quantidade);
		custo_frete += (1 - desconto) * frete;

		if (desconto != 0)
		{
			clientes_com_desconto++;
			clientes++;
		}
		else
		{
			clientes++;
		}

		printf("Frete com desconto: R$%.2f", custo_frete);

		codigo = obter_codigo();
	}

	printf("%.2f%% dos clientes obtiveram desconto", 100*clientes_com_desconto / clientes);

	return 0;
}