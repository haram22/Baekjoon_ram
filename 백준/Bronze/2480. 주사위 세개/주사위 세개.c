#include <stdio.h>
/*
3개의 변수 설정
세 변수가 모두 같은 경우
-> 10000+눈*1000
같은 눈이 두개인 경우
-> 1000+눈*100
모두 다른 경우
-> 가장 큰 눈*100
가장 큰 눈 구하는 방법
-> 반복문으로 한 수를 가장 크다고 두고 비교
*/
int main(void) {
  int num[3]={0};
  int result=0;
  scanf("%d %d %d", &num[0], &num[1], &num[2]);
  if(num[0]==num[1] && num[0]==num[2] && num[1]==num[2]){
    result = 10000+num[1]*1000;
  }
  else if(num[0]==num[1] && num[1]!=num[2]){
    result = 1000+num[1]*100;
  }
  else if(num[1]==num[2] && num[1]!=num[0]){
    result = 1000+num[1]*100;
  }
  else if(num[0]==num[2] && num[2]!=num[1]){
    result = 1000+num[2]*100;
  }
  else {
    int big = num[0];
    for(int i=0;i<3;i++){
      if(big <= num[i]) big = num[i];
    }
    result = big*100;
  }
  
  printf("%d", result);
  return 0;
}