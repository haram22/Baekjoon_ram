#include <stdio.h>

int main(void) {
  //x와 y 각각의 좌표를 입력받기 위한 변수
  int x,y;
  //x와 y 좌표 입력받기
  scanf("%d %d", &x,&y);
  //조건문으로 입력받은 좌표가 몇 사분면인지 검사하고, 출력하기
    if(x>0) {
      if(y>0) printf("1");
      else printf("4");
    }
    else {
      if(y>0) printf("2");
      else printf("3");
    }
  return 0;
}