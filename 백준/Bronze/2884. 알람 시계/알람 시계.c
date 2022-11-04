#include <stdio.h>

int main(void) {
  int hour;
  int min;
  scanf("%d %d", &hour, &min);
  if(min - 45 < 0) {
    if(hour == 0) {
      hour = 23;
      min = 60-(45 - min);
      }
    else{
      hour--;
      min = 60-(45 - min);
    }
  }
  else min = min - 45;
  printf("%d %d", hour, min);
  return 0;
}