#include <stdio.h>
#include <math.h>

float piSeries(int n)
{
	float PI = 0;

	for (int i = 0; i < n; i++)
		PI += 4.0 / (2 * i + 1) * pow(-1, i);

	return PI;
}

int main(void)
{
	int termos;

	printf("Digite o numero de termos da seria de Gregory-Leibniz: ");
	scanf("%d", &termos);
	printf("Gregory-Leibniz Series: PI = %.10lf", piSeries(termos));

	return 0;
}