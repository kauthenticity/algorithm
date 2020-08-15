#include <iostream>
#include <queue>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	queue<int> q;
	int n, k, temp;

	cin >> n >> k;

	// queue initialization
	for (int i = 1; i <= n; i++) {
		q.push(i);
	}

	cout << "<";
	while (!q.empty()) {
		for (int i = 0; i < k - 1; i++) {
			q.push(q.front());
			q.pop();
		}
		temp = q.front();
		q.pop();

		if (q.empty()) {
			cout << temp << ">";
		}
		else {
			cout << temp << ", ";
		}
	}

	
	return 0;
}