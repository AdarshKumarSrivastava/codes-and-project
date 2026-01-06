#include <stdio.h>
#include <string.h>

int main() {
    char a[1000];
    int i, num_c = 0, num_w = 0;
    int in_word = 0;

    printf("Enter a sentence: ");
    fgets(a, sizeof(a), stdin);

    for (i = 0; a[i] != '\0'; i++) {
        if (a[i] != '\n') { 
            num_c++;
        }
        if (a[i] != ' ' && a[i] != '\n' && !in_word) {
            in_word = 1;
            num_w++;
        } else if (a[i] == ' ' || a[i] == '\n') {
            in_word = 0;
        }
    }
    printf("Number of characters: %d\n", num_c);
    printf("Number of words: %d\n", num_w);

    return 0;
}


// Copy of string using function ###########################################3
#include <stdio.h>
#include <string.h>

int main() {
    char str1[100], str2[100];

    printf("Enter a string: ");
    fgets(str1, sizeof(str1), stdin);
    strcpy(str2, str1);
    printf("Original string: %s", str1);
    printf("Copied string: %s", str2);

    return 0;
}
// Copy of string without function
#include <stdio.h>

int main() {
    char str1[100], str2[100];
    int i;

    printf("Enter a string: ");
    fgets(str1, sizeof(str1), stdin);
    for (i = 0; str1[i] != '\0'; i++) {
        str2[i] = str1[i];
    }
    str2[i] = '\0'; 
    printf("Original string: %s", str1);
    printf("Copied string: %s", str2);

    return 0;
}
//concat of two names string #####################
#include <stdio.h>
#include <string.h>

int main() {
    char firstName[50], lastName[50], fullName[100];
    printf("Enter first name: ");
    scanf("%s", firstName);

    printf("Enter last name: ");
    scanf("%s", lastName);
    strcpy(fullName, firstName);
    strcat(fullName, " ");
    strcat(fullName, lastName);
    printf("Full name: %s", fullName);

    return 0;
}
// Concat without function#####################
#include <stdio.h>

int main() {
    char firstName[50], lastName[50], fullName[100];
    int i, j;

    printf("Enter first name: ");
    scanf("%s", firstName);
    printf("Enter last name: ");
    scanf("%s", lastName);

    for (i = 0; firstName[i] != '\0'; i++) {
        fullName[i] = firstName[i];
    }
    fullName[i] = ' ';
    i++;
    for (j = 0; lastName[j] != '\0'; j++, i++) {
        fullName[i] = lastName[j];
    }
    fullName[i] = '\0';
    printf("Full name: %s\n", fullName);

    return 0;
}
// Write a program to sort 5 string words in a array
#include <stdio.h>
#include <string.h>

int main() {
    char words[5][50], temp[50];
    int i, j;
    printf("Enter 5 words:\n");
    for (i = 0; i < 5; i++) {
        scanf("%s", words[i]);
    }

}