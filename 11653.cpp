#include <iostream>
#include <cmath>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int n, i, t;
	cin >> n;

	t = n;

	for (i = 2; i*i <= n; ) {
		if (n % i == 0) {
			cout << i << "\n";
			n /= i;
		}
		else {
			i++;
		}
	}
	if (n != (int)sqrt(t)) {
		cout << n << "\n";
	}
	else if (n == i) {
		cout << n << "\n";
	}
	return 0;
}