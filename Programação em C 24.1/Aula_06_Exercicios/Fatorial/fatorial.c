#include <stdio.h>

int main(void)
{
	int n, k;

	printf("Digite o inteiro no qual quer calcular o fatorial: ");
	scanf("%d", &n);

	for (k = n - 1; k > 0; k--)
		n *= k;
	printf("%d", n);

	return 0;
}