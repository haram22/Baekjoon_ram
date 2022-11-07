#include <stdio.h>

int main(void) {
  int num;
  scanf("%d", &num);
  for(int i=0; i<num; i++){
    for(int j=num-i-2; j>=0; j--){
      printf(" ");
    }
    for(int j=0; j<=i; j++){
      printf("*");
    }
    printf("\n");
  }
}