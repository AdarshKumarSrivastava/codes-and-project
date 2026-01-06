#include<stdio.h>
void sd(){
    printf("Hello World");
} 
int main(){
    sd();
    return 0;
}
#include<stdio.h>
int add(int a){
    printf("HY %d", a);
}
int main(){
    int c=add(20);
    return 0;
}

#include<stdio.h>
int ret(){
    return 20;
}
int main(){
    int b=20+ret();
    printf("%d",b);
    return 0;
}

#include<stdio.h>
int sum(int a,int b){
    int c=a+b;
    return c;
}

int main(){
    int s=sum(10,20);
    printf("%d",s);
    return 0;
}

// ###########################
int calculation(int n){
    if(n==0){
        return 0;
    }
    return n + calculation(n-1);
}
#include<stdio.h>
int main(){
    int cal=calculation(50);
    printf("%d",cal);
}
// ########################
int fibo(int n){
    if(n==0){
        return 0;
    }
    if(n==1){
        return 1;
    }
    return fibo(n-1)+fibo(n-2);
}
#include<stdio.h>
int main(){
    int fib=fibo(20);
    printf("%d",fib);
    return 0;
}
