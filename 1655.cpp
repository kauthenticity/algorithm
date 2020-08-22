#include <iostream>
#include <queue>
#include <functional>

using namespace std;


int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n, val;
	priority_queue <int, vector<int>, less<int>> maxheap;
	priority_queue <int, vector<int>, greater<int>> minheap;

	cin >> n;
	cin >> val;
	maxheap.push(val);
	cout << maxheap.top() << "\n";

	for (int i = 1; i < n; i++) {
		cin >> val;

		if (maxheap.size() == minheap.size()) {
			if (val < minheap.top()) {
				maxheap.push(val);
			}
			else {
				int temp = minheap.top();
				minheap.pop();
				maxheap.push(temp);
				minheap.push(val);
			}
		}
		else {
			if (val >= maxheap.top()) {
				minheap.push(val);
			}
			else {
				int temp = maxheap.top();
				maxheap.pop();
				minheap.push(temp);
				maxheap.push(val);
			}
		}

		cout << maxheap.top() << "\n";
	}

	return 0;
}