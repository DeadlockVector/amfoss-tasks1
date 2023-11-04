#include <stdio.h>

int main () {

    int n;
    printf("Enter the number - ");
    scanf("%d", &n);

    for (int i = 0; i<n; i++) {

        int factors = 1;

        for (int j = 2; j<i+1; j++) {
            if (i%j==0) {
                factors++;
            }
        }

        if (factors == 2) {
            printf("%d is a prime number\n", i);
        }
    }

    return 0;

}