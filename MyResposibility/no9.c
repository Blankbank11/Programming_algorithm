#include<stdio.h>

int main(){
    int N,M,Y,A,B;
    printf("Enter value of N M Y: ");
    scanf("%d%d%d",&N,&M,&Y);
  
    B = ((Y*M)+N-Y)/(M-1);
    A = B+N;

   printf("N M Y --> %d %d %d\n",N,M,Y);
   printf("A B --> %d %d\n",A,B);
}