#include <iostream>
#include <deque>
#include <queue>

using namespace std;

int find_index(deque<int> dq, int cur) {
	for (int i = 0; i < dq.size(); i++) {
		if (dq[i] == cur) {
			return i;
		}
	}
}
int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	int n, m, val, cnt = 0;
	queue<int> q;
	deque<int> dq;
	cin >> n >> m;

	for (int i = 1; i <= n; i++) {
		dq.push_back(i);
	}

	for (int i = 0; i < m; i++) {
		cin >> val;
		q.push(val);
	}

	while (!q.empty()) {
		int cur = q.front();
		if (cur == dq.front()) {
			dq.pop_front();
			q.pop();
		}

		else {
			int idx = find_index(dq, cur);
			if (idx <= dq.size() / 2) {
				dq.push_back(dq.front());
				dq.pop_front();
				cnt++;
			}
			else {
				dq.push_front(dq.back());
				dq.pop_back();
				cnt++;
			}
		}
	}

	cout << cnt << "\n";
	return 0;
}