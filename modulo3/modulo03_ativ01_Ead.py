'''




'''


int main() {
    float n1, n2;
    
    printf("Digite o primeiro numero: ");
    scanf("%f", &n1);
    
    printf("Digite o segundo numero: ");
    scanf("%f", &n2);
    
    printf("Soma: %.2f\n", n1 + n2);
    printf("Diferenca: %.2f\n", n1 - n2);
    printf("Multiplicacao: %.2f\n", n1 * n2);
    
    if (n2 != 0) {
        printf("Divisao: %.2f\n", n1 / n2);
    } else {
        printf("Divisao por zero nao permitida\n");
    }
    
    return 0;
}