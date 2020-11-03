#include <stdio.h>
#include <iostream>
using namespace std;

int main(){
	int x, c, i;
	cin >> x >> c;
	int a[x];
	for(i = 0; i < x; i++) {
	cin >> a[i];
}
	for(i = 0; i <= x; i++){
		if(c > a[i]){
			cout << a[i] << " ";
		}
	}
	return 0;
}
