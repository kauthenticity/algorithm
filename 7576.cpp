#include <iostream>
#include <queue>

using namespace std;

int n, m;
int tom[1000][1000];
int dx[4];
int dy[4];

bool is_inside(int x, int y) {
	// checking if current location is involved in box
	return((x >= 0  && x < n) && (y >= 0 && y < m));
}

bool is_ripe() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (tom[i][j] == 0) {
				return false;
			}
		}
	}

	return true;
}

int go() {
	queue<pair<int, int>> q;
	int day = 0;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (tom[i][j] == 1) {
				q.push(pair<int, int>(i, j));
			}
		}
	}

	while (!q.empty()) {
		day++;
		int qsize = q.size();
		for (int i = 0; i < qsize; i++) {
			int curx = q.front().first;
			int cury = q.front().second;
			q.pop();

			for (int j = 0; j < 4; j++) {
				int newx = curx + dx[j];
				int newy = cury + dy[j];

				if (tom[newx][newy] == 0 && is_inside(newx, newy)) {
					tom[newx][newy] = 1;
					q.push(pair<int, int>(newx, newy));
				}
			}
		}
	}
	if (is_ripe()) {
		return day-1;
	}
	else {
		return -1;
	}
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> m >> n;

	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++) {
			cin >> tom[i][j];
		}
	} // input

	dx[0] = -1; dx[1] = 0; dx[2] = 1; dx[3] = 0;
	dy[0] = 0; dy[1] = 1; dy[2] = 0; dy[3] = -1;
	// direction initialization

	cout << go() << "\n";

	return 0;
}