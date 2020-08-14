#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

long long int dp[101][100001];

#define max(a, b) ((a)>(b) ? (a) : (b))

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n, w, v, k;

	vector <pair <int, int>> knapsack;
	// knapsack.first : weight
	// knapsack.second : value

	cin >> n >> k;
	// n : # of the objects
	// k : weight that bag can carry

	knapsack.push_back(make_pair(0, 0));
	for (int i = 0; i < n; i++) {
		cin >> w >> v;
		knapsack.push_back(make_pair(w, v));
	}

	sort(knapsack.begin(), knapsack.end());

	for (int j = 0; j < knapsack[1].first; j++) {
		dp[1][j] = 0;
	}

	for (int j = knapsack[1].first; j <= k; j++) {
		dp[1][j] = knapsack[1].second;
	}

	for (int i = 2; i <= n; i++) {
		for (int j = 1; j <= k; j++) {
			int cur_weight = knapsack[i].first;
			int cur_profit = knapsack[i].second;

			if (cur_weight <= j) {
				dp[i][j] = max(dp[i - 1][j], cur_profit + dp[i - 1][j - cur_weight]);
			}
			else dp[i][j] = dp[i - 1][j];
		}
	}

	cout << dp[n][k] << "\n";

	return 0;
}