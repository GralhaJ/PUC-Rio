#include <stdio.h>

void le_dados(int *p1) {

	scanf("%d", p1);
}

void maior(int a, int b, int* p2) {

	if (a >= b) {
		(*p2) = a;
	}
	else {
		(*p2) = b;
	}
}

float calculos(int num1, int num2, int* p3) {

	(*p3) = num1 + num2;
	float media = (float)(*p3) / 2;

	return media;
}