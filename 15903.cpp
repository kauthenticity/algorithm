#include <iostream>
#include <queue>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	long long int t, sum = 0;
	int n, m;
	priority_queue<long long int, vector<long long int>, greater<long long int>> card;


	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		cin >> t;
		card.push(t);
		sum += t;
	}
	for (int i = 0; i < m; i++) {
		long long int min, second_min, temp_sum;

		min = card.top();
		card.pop();
		second_min = card.top();
		card.pop();

		temp_sum = min + second_min;

		card.push(temp_sum);
		card.push(temp_sum);

		sum += temp_sum;
	}

	cout << sum << "\n";

	return 0;
}