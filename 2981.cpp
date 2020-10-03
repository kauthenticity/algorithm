#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

#define MAX 101
#define INF 2100000000
#define min(x, y) ((x)<(y)?(x):(y))

int n;
int arr[MAX];
int quotient[MAX];
int difference[5000];
int idx = 0;

int gcd(int a, int b) {
	if (a == 0) {
		return b;
	}
	else {
		return gcd(b%a, a);
	}
}

int findGCD() {
	int result = difference[0];

	for (int i = 1; i < idx; i++) {
		if (difference[i] < result) {
			result = gcd(difference[i], result);
		}
		else {
			result = gcd(result, difference[i]);
		}
		if (result == 1) {
			return 1;
		}
	}

	return result;
}

void calc_difference() {
	idx = 0;
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			difference[idx++] = abs(arr[i] - arr[j]);
		}
	}
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n;

	int min = INF;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		if (arr[i] < min) {
			min = arr[i];
		}
	}
	calc_difference();

	int gcd = findGCD();

	vector<int> v;

	for (int i = 2; i <= sqrt(gcd); i++) {
		if (gcd % i == 0) {
			if (gcd / i == i) {
				cout << i << " ";
			}
			else {
				cout << i << " ";
				v.push_back(gcd / i);
			}
		}
	}
	for (int i = v.size() - 1; i >= 0; i--) {
		cout << v[i] << " ";
	}

	cout << gcd;

	return 0;
}
