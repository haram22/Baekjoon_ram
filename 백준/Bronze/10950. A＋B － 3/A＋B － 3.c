#include <stdio.h>
int main(void) {
  int num;
  scanf("%d", &num);
  int input1[num], input2[num], sum[num];
  for(int i=0; i<num; i++){
    scanf("%d %d", &input1[i], &input2[i]);
    sum[i] = input1[i] + input2[i];
  }
  for(int i=0; i<num; i++){
    printf("%d\n", sum[i]);
  }
}