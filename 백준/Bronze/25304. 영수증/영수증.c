#include <stdio.h>

int main(void) {
  int inputsum=0, num=0;
  int sum=0;

  scanf("%d %d", &inputsum, &num);
  int price[num];
  int many[num];
  for(int i=0; i<num; i++){
    scanf("%d %d", &price[i], &many[i]);
  }
  for(int j=0; j<num; j++){
    sum += price[j]  * many[j];
  }
  if(inputsum == sum) printf("Yes\n");
  else printf("No\n");
}