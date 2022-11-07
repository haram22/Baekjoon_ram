#include <stdio.h>

int main(void) {
  int num1, num2;
  
  while(scanf("%d %d", &num1, &num2)!=EOF){
    printf("%d\n", num1+num2);
    if(num1 < 0 || num1 >= 10) return 0;
    if(num2 < 0 || num2 >= 10) return 0;
  }
}