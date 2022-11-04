#include <stdio.h>
#include <stdlib.h>
//#include "stack.h"

/*
먼저 몇 개의 수를 입력할지 입력받기
n개만큼 수 입력하기
입력받은 수 배열에 하나씩 저장
저장할 때 다음 수가 0이면 앞 수 지우기
- 그 다음 수가 또 0이면 앞 수 지우기
남은 수들 합 구하기

0을 입력받자마자 앞 수 지우기
남은 것들 배열에 저장.
합 구하기
*/

int main(void) {
  int len=0;
  int arr[1000000];
  int put;
  int sum=0;
  scanf("%d",&put);
  int st[put];

  for(int i=0;i<put;i++){
    scanf("%d",&st[i]);

    if(st[i]!=0)  {
      arr[len]=st[i];
      len++;
    }
    else {
      len--;
      arr[len]=0;
    }
  }

  for(int i=0;i<len;i++){
    sum+= arr[i];
  }
    printf("%d ",sum);

  return 0;
}
