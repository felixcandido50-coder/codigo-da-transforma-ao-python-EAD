'''




'''


int main() {
    int n1, n2;
    
    printf("Digite o primeiro numero: ");
    scanf("%d", &n1);
    
    printf("Digite o segundo numero: ");
    scanf("%d", &n2);
    
    if (n1 > n2) {
        printf("O maior e: %d\n", n1);
    } else if (n2 > n1) {
        printf("O maior e: %d\n", n2);
    } else {
        printf("Os dois numeros sao iguais.\n");
    }
    
    return 0;
}