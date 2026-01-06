#include<stdio.h>
int main(){
    int day;
    printf("enter day number (1-7)=");
    scanf("%d",&day);
    switch (day)
    {
    case 1:
        printf("Monday");
        break;
    case 2:
        printf("Tuesday");
        break;
    case 3:
        printf("Wednesday");     
        break;
    case 4:
        printf("Thusday");     
        break;    
    case 5:
        printf("Friday");     
        break;    
    case 6:
        printf("Saturday");     
        break;    
    case 7:
        printf("Sunday");     
        break;    
    default:
        printf("Not in Range");
        break;
    }
}


#include<stdio.h>
int main(){
    int a;
    printf("Enter 1 - Addition of Two Number\n");
    printf("Enter 2 - Subtraction of Two Number\n");
    printf("Enter 3 - Multiplication of Two Number\n");
    printf("Enter 4 - Division of Two Number\n");
    printf("Enter Any Option you want =");
    scanf("%d",&a);
    int b; 
    int c;
    printf("Enter First Number =");
    scanf("%d",&b);
    printf("Enter Second Number =");
    scanf("%d",&c);
    switch (a)
    {
    case 1:
        printf("Addition = %d",b+c);
        break;
    case 2:
        printf("Subtration = %d",b-c);
        break;
    case 3:
        printf("Multiplication =%d ",b*c);
        break;    
    case 4:
        printf("Division = %d",b/c);
        break;    
    default:
        printf("Invalid");
        break;
    }
}

#include<stdio.h>
int main(){
    int marks;
    printf("Enter Marks =");
    scanf("%d",&marks);
    int t=marks/10;
    switch (t)
    {
    case 10:
    case 9:
        printf("A");
        break;
    case 8:
    case 7:
        printf("B");
        break;
    case 6:
    case 5:
        printf("C");
        break;
    case 4:
    case 3:
        printf("D");
        break;           
    default:
        printf("Fail");
        break;
    }
}