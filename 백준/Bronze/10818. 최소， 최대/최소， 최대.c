#include <stdio.h>

int main(void) {
  int a;
  int max=-1000000;
  int min=1000000;
  scanf("%d",&a);
  int num[a];
  for(int i=0;i<a;i++){
    scanf("%d",&num[i]);
  }
  for(int i=0;i<a;i++){
    if(max<num[i]) max=num[i];
    if(min>num[i]) min=num[i];
  }
  printf("%d %d",min,max);
  return 0;
}