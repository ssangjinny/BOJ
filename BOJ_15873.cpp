#include <iostream>

using namespace std;

int main(){
	int a, b;
	cin >> a;
	if (a == 1010) b = 20;
	else if(a >= 100 && (a % 10) == 0){
		b = (a/100) + (a%100);
	}
	else if(a >= 100 && (a % 10) != 0){
		b = (a/10) + (a%10);
	}
	else b = (a/10) + (a%10);
	cout << b;
}
