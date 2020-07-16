#include <iostream>

using namespace std;

int n;
int maze[100][100];
long long dp[100][100];

void go() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (i == n - 1 && j == n - 1) break;
			if (dp[i][j] != 0) {
				if (i + maze[i][j] < n) {
					dp[i + maze[i][j]][j] += dp[i][j];
				}
				if (j + maze[i][j] < n) {
					dp[i][j + maze[i][j]] += dp[i][j];
				}
			}
		}
	}
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> maze[i][j];
			dp[i][j] = 0;
		}
	}

	dp[0][0] = 1;

	go();

	cout << dp[n-1][n-1] << "\n";


	return 0;
}