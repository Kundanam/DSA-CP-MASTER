#include<stdio.h>
int factorial(int );
void main(){
    int x;
    scanf("%d",&x);
    printf("%d",factorial(x));
}
int factorial(int a){
    if (a==1){
        return 1;
    }
    return a*factorial(a-1);
       
}
