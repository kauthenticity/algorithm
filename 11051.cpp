#include <iostream>

using namespace std;

int comb[1001][1001];

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int n, k;

	cin >> n >> k;

	for (int i = 0; i <= n; i++) {
		comb[0][i] = 0;
		comb[i][0] = 1;
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= k; j++) {
			comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
		}
	}

	cout << comb[n][k];

	return 0;
}
