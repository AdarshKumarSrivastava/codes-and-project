// Area of rectangle
#include<stdio.h>
int main(){
    int a;
    int b;
    int area;
    printf("Enter length and breadth");
    scanf("%d %d",&a,&b);
    area=a*b;
    printf("%d",area);
    return 0;
}

// Print your name 
#include<stdio.h>
int main(){
    char a;
    printf("Enter Your Name\n");
    scanf("%c",&a);
    printf("%c",a);
    return 0;
}

// Add two numbers
#include<stdio.h>
int main(){
    int a;
    int b;
    int sum;
    printf("Enter 1st and 2nd number for addition\n");
    scanf("%d %d",&a,&b);
    sum=a+b;
    printf("%d",sum);
    return 0;
}

// Find square
#include<stdio.h>
int main(){
    int a;
    int square;
    printf("Enter no. to find Square\n");
    scanf("%d",&a);
    square=a*a;
    printf("Square %d",square);
    return 0;

}
// Swap of Number
#include<stdio.h>
int main(){
    int a;
    int b;
    int c;
    printf("Enter two number to Swap it!!\n");
    scanf("%d %d",&a,&b);
    c=a;
    a=b;
    b=c;
    printf("Swaped a=%d",a);
    printf("Swaped b=%d",b);
    return 0;
}
// Covert Temperature
#include<stdio.h>
int main(){
    float c;
    float convert;
    printf("Enter temp in celsius to Fahrenheit\n");
    scanf("%f",&c);
    convert=(1.8*c)+32;
    printf("%2f",convert);
    return 0;
}

// Simple Interest
#include<stdio.h>
int main(){
    float p;
    float r;
    float t;
    float si;
    printf("Enter Principal Amount\n");
    scanf("%f",&p);
    printf("Enter Interest Rate\n");
    scanf("%f",&r);
    printf("Enter Time Period\n");
    scanf("%f",&t);
    si=(p*r*t)/100;
    printf("Total Interest%3f\n=",si);
    float total;
    total=si+p;
    printf("Total Amount after interest %3f\n",total);
    return 0;
}
// Average
#include<stdio.h>
int main(){
    int a;
    int b;
    int c;
    int avg;
    printf("Enter three number to find Average\n");
    scanf("%d %d %d",&a,&b,&c);
    avg=(a+b+c)/3;
    printf("Average of Three Numbers=%d",avg);
    return 0;
}
// 5 apple 12rs and 7oranges at 7rs find profit
#include<stdio.h>
int main(){
    int apple;
    int oranges;
    int Ta;
    int To;
    int total;
    printf("Number of apple sold\n");
    scanf("%d",&apple);
    printf("Number of Oranges sold\n");
    scanf("%d",&oranges);
    Ta=apple*12;
    To=oranges*7;
    total=Ta+To;
    printf("Total prices of apple=%d\n",Ta);
    printf("Total prices of apple=%d\n",To);
    printf("Total Earn=%d\n",total);
    return 0;
}
