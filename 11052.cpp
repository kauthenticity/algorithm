#include <iostream>
#include <algorithm>

using namespace std;

int n;
int price[1001];
int dp[1001];

void go() {
	for (int i = 2; i <= n; i++) {
		dp[i] = price[i];
		for (int j = 1; j < i; j++) {
			dp[i] = max(dp[i], dp[j] + price[i - j]);
		}
	}
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> price[i];
	}
	dp[1] = price[1];
	go();
	cout << dp[n] << "\n";

	return 0;
}