#include <iostream>

using namespace std;

long long int pow(int a, int x, int c) {
	if (x == 1) {
		return a%c;
	}
	else if (x % 2 == 0) {
		long long int temp = pow(a, x / 2, c);
		temp %= c;
		return (temp * temp)%c;
	}
	else {
		return ((a%c) * (pow(a, x - 1, c)%c))%c;
	}
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int a, b, c;
	
	cin >> a >> b >> c;

	cout << pow(a, b, c)%c << "\n";

	return 0;
}