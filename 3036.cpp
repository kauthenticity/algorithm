#include <iostream>
#include <vector>

using namespace std;

#define MAX 101

int n;
int ring[MAX];
int first;

vector<pair<int, int>> res;

int calcGCD(int a, int b) {
	if (b == 0) {
		return a;
	}
	else {
		return calcGCD(b, a % b);
	}
}

void go() {
	for (int i = 0; i < n; i++) {
		int gcd = calcGCD(first, ring[i]);

		res.push_back(pair<int, int>(first / gcd, ring[i] / gcd));
	}
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	cin >> first;

	n--;

	for (int i = 0; i < n; i++) {
		cin >> ring[i];
	}

	go();

	for (int i = 0; i < n; i++) {
		cout << res[i].first << "/" << res[i].second << "\n";
	}
	

	return 0;
}
