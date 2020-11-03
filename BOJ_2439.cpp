#include <stdio.h>
#include <iostream>
using namespace std;

int main(){
	int x, c, f;
	cin >> x;
	for(c = 1; c <= x; c++){
		for(f = 1; f <= x - c; f++){
			cout << " ";
		}
		for(f = 0; f < c; f++){
		cout << "*";
		}
		cout << '\n';
	}
	return 0;
}
