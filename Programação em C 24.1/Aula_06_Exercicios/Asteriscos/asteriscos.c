#include <stdio.h>

int main(void)
{
	int i;

	printf("Entre com um inteiro: ");
	scanf("%d", &i);

	for (int k = 0; k < i; k++)
	{
		for (int k = 0; k < i; k++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}