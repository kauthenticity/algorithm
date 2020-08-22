#include <iostream>
#include <queue>
#include <functional>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	priority_queue <pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minheap;
	int n, x, sign;

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> x;
			if (x != 0) {
				if (x < 0) {
					x = -x;
					sign = -1;
				}
				else {
					sign = 1;
				}

				minheap.push(pair<int, int>(x, signs));
			}
			else {
				if (minheap.empty()) {
					cout << "0\n";
				}
				else {
					int top = minheap.top().first;
					sign = minheap.top().second;
					cout << top * sign << "\n";
					minheap.pop();
				}
			}
	}
	return 0;
}