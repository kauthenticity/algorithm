#include <iostream>

using namespace std;

int calcGCD(int a, int b) {
	if (b == 0) {
		return a;
	}
	else {
		return calcGCD(b, a % b);
	}
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int a, b;

	cin >> a >> b;

	int gcd = calcGCD(a, b);
	int lcm;

	double aa = a / gcd;
	double bb = b / gcd;

	if (aa < 0) {
		lcm = a * bb;
	}
	else {
		lcm = b * aa;
	}
	
	cout << gcd << "\n" << lcm << "\n";

	return 0;
}
