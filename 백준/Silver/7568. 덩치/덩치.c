#include <stdio.h>

struct bmi{
  int weight;
  int height;
};

int main(void) {
  int num;
  scanf("%d",&num);
  int count[num];

  for(int i=0;i<num;i++) count[i]=0;
  
  struct bmi list[num];

  for(int i=0;i<num;i++){
    scanf("%d %d",&list[i].weight, &list[i].height);
  }

  for(int i=0;i<num;i++){
    for(int j=0;j<num;j++){
      if((list[i].weight < list[j].weight) && (list[i].height < list[j].height)) count[i]++;
    }
    printf("%d ",count[i]+1);
  }
  return 0;
}