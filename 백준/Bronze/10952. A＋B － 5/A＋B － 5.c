#include <stdio.h>

int main(void) {
  int num1, num2;
  int sum[100];
  int count=0;
  
  while(1){
    scanf("%d %d", &num1, &num2);
    if(num1 == 0 || num2 == 0) break;
    sum[count++] = num1+num2;
    if(num1 < 0 || num1 >= 10) return 0;
    if(num2 < 0 || num2 >= 10) return 0;
  }
  
  for(int i=0; i<count; i++){
    printf("%d\n", sum[i]);
  }
}