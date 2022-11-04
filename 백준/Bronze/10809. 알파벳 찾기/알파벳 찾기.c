#include <stdio.h>
#include <string.h>

int main(void) {
  char st[100];
  char alpha[26];
  scanf("%s",st);
  for(int j=0;j<26;j++){
    for(int i=0;i<strlen(st);i++){
      if(st[i]==97+j) {
        alpha[j]=i;
        break;
      }
      else alpha[j]=-1;
    }
  }
  for(int i=0;i<26;i++){
    printf("%d ",alpha[i]);
  }
  return 0;
}