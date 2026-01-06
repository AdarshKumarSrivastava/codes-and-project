#include<stdio.h>
int main(){
    int a[5];
    printf("Enter elements\n");
    for(int i=0;i<a;i++){
        scanf("%d",&a[i]);
    }
    for(int i=0;i<a;i++){
        printf("%d\n",a[i]);
    }
    return 0;
}
// ###########################
#include<stdio.h>
int main(){
    int n;
    printf("Enter number of elements you want in array");
    scanf("%d",&n);
    int a[n];
    printf("Enter elements\n");
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(int i=0;i<n;i++){
        printf("Value of %d index element=%d\n",i,a[i]);
        printf(" Address of element=%d\n",&a[i]);
    }
    return 0;
}
// ##################################
#include<stdio.h>
int main(){
    int n;
    printf("Enter number of elements you want in array");
    scanf("%d",&n);
    int a[n];
    printf("Enter elements\n");
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    int max=a[0];
    int min=a[0];
    for(int i=1;i<n;i++){
        if(a[i]>max){
            max=a[i];
        }
        else if(a[i]<min){
            min=a[i];
        }
    }
    printf("Maximum no.=%d",max);
    printf("Manimum no.=%d",min);
    return 0;
}