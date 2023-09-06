#include <stdio.h>
#include "header.h"

int main(void)
{
	int num1, num2, max, soma;
	printf("Informe um numero inteiro: ");
	le_dados(&num1); // captura um número do teclado
	printf("Informe outro numero inteiro: ");
	le_dados(&num2);
	maior(num1, num2, &max); // armazena em max o maior valor entre eles
	printf("O maior numero eh %d\n", max);
	printf("A media dos numeros eh %.1f\n", calculos(num1, num2, &soma)); // obs
	printf("A soma dos numeros eh %d ", soma);
	return 0;
}
