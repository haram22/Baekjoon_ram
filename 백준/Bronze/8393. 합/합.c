#include <stdio.h>
int main(void) {
  int input, sum=0;
  scanf("%d", &input);
  if (input <1 || input>10000) return 0;
  for(int i=1; i<=input; i++){
    sum += i;
  }
  printf("%d\n", sum);
}