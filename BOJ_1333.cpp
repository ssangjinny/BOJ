#include <iostream>
#include <stdio.h>

using namespace std;

int main(){
	int N, L, D, count;
	int time = 0;
	scanf("%d %d %d", &N, &L, &D);
	for(int a = 1; a <= N; a++){
		while(time <= L*a) time++;
		for (time; L*a < time <= (L*a)+5; time++){
			if (time == D*a){
				printf("%d", D*a);
				count++;
				break;
			}
		}
		if(count == 1) break;
	}
	if(count == 0) printf("%d", D*N);
}
