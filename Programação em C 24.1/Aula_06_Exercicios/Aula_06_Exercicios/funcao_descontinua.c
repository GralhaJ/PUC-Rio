#include <stdio.h>

float f(float x)
{
	if (x <= 1)
		return x * x;
	else
		return 6 - x;
}

int main(void)
{
	float valor_inicial;
	float delta;
	int pontos;

	printf("Entre com o valor inicial, o incremento e o numero maximo de pontos: ");
	scanf("%f %f %d", &valor_inicial, &delta, &pontos);
	printf("x  \tf(x)\n");
	for (int i = 0; i < pontos; i++, valor_inicial += delta)
		printf("%7.2f\t%7.2f\n", valor_inicial, f(valor_inicial));

	return 0;
}