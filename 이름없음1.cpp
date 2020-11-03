#include <iostream>
using namespace std;

int main(){
	int a, b, c, count = 0;
	cin >> a;
	b = a;
	while(a != b){
	if(a/10 == 0){
		a = a + a;
	}
	else{
		c = (a%10) + ((a-(a%10))/10);
		a = (a%10) + (c%10);
	}
	count++;
}
	cout << count;
}
