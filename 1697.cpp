#include <iostream>
#include <queue>

using namespace std;

int n, k;
queue<int> q;
int dir[2];
int sec[100001] = { 0, };

void go() {
	bool flag = false;
	q.push(n);

	while (!flag) {
		int size = q.size();
		for (int i = 0; i < size; i++) {
			int x = q.front();
			q.pop();

			if (x == k) {
				flag = true;
				break;
			}

			for (int j = 0; j < 2; j++) {
				int newx = x + dir[j];

				if (newx < 0 || newx>1000000) {
					continue;
				}

				if (!sec[newx]) {
					sec[newx] = sec[x] + 1;
					q.push(newx);
				}
			}
			int newx = x * 2;
			if (newx > 100000) {
				continue;
			}
			if (!sec[newx]) {
				sec[newx] = sec[x] + 1;
				q.push(newx);
			}
		}
	}
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n >> k;

	dir[0] = 1;
	dir[1] = -1;

	go();

	cout << sec[k] << "\n";

	return 0;
}