#include <stdio.h>

int main(void) {
  int input;
  scanf("%d", &input);
  if(input<1 || input>9) return 0;
  else{
    for(int i=1; i<10; i++){
      printf("%d * %d = %d\n", input, i, input*i);
    }
  }
}