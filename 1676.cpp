#include <iostream>

using namespace std;

#define min(x, y) ((x)<(y)?(x):(y))

int get_five(int n) {
	long long int cnt = 0;

	for (int i = 5; i <= n; i *= 5) {
		cnt += n / i;
	}

	return cnt;
}

int get_two(int n) {
	long long int cnt = 0;

	for (int i = 2; i <= n; i *= 2) {
		cnt += n / i;
	}

	return cnt;
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int n;
	long long int five=0, two=0;

	cin >> n;

	five = get_five(n);
	two = get_two(n);

	cout << min(five, two) << "\n";

	return 0;
}
