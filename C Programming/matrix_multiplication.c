#include <stdio.h>
int main(){
    int matrix[3][3];
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            int entry;
            printf("Provide entries:");
            scanf("%d", &entry);
            matrix[i][j] = entry;
        }
    }

    for (int i = 0; i < 3; i++){
        int productMatrix[3][3];
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                productMatrix[i][j] = 0;
                for (int k = 0; k < 3; k++){
                    productMatrix[i][j] += matrix[i][k] * matrix[k][j];
                }
            }
        }
        for (int j = 0; j < 3; j++){
            printf("%d\n", productMatrix[i][j]);
        }
    }
    return 0;
}