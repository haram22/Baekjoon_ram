#include <stdio.h>

int main(void) {
  int total;
  
  scanf("%d", &total);
  int input1[total];
  int input2[total];
  int sumarr[total];
  int sum;
  
  for(int i=0; i<total; i++){
    sum=0;
    scanf("%d %d", &input1[i], &input2[i]);
    sum+= input1[i] + input2[i];
    sumarr[i] = sum;
  }

  for(int i=0; i<total; i++){
    printf("%d\n", sumarr[i]);
  }
}