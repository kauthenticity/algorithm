#include <iostream>
#include <queue>

using namespace std;

int n, m;
short int maze[102][102];
int dist[102][102] = {0, };
//bool visited[102][102] = { false , };
int dx[4];
int dy[4];

int go() {
	queue<pair<int, int>> q;
	
	int x, y;

	q.push(pair<int, int>(1, 1));
	
	x = y = 1;
	dist[x][y] = 1;
	while (!q.empty()) {
		int newx, newy;

		x = q.front().first;
		y = q.front().second;
		q.pop();

		if (x == n && y == m) break;


		for (int k = 0; k < 4; k++) {
			newx = x + dx[k];
			newy = y + dy[k];

			if ((maze[newx][newy] == 1) && (dist[newx][newy] == 0) && (newx<=n && newy<=m)) {
				q.push(pair<int, int>(newx, newy));
				dist[newx][newy] = dist[x][y] + 1;
			}
		}
	}

	return dist[n][m];
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	string str;
	
	cin >> n >> m;

	for (int i = 0; i < n + 2; i++) {
		maze[i][0] = maze[i][m + 1] = 0;
	}
	for (int i = 0; i < m + 2; i++) {
		maze[0][i] = maze[n + 1][0] = 0;
	}

	for (int i = 1; i <= n; i++) {
		cin >> str;
		for (int j = 1; j <= m; j++) {
			maze[i][j] = str[j-1]-'0';
		}
	}
	
	dx[0] = -1; dx[1] = 0; dx[2] = 1; dx[3] = 0;
	dy[0] = 0; dy[1] = 1; dy[2] = 0; dy[3] = -1;


	cout << go() << "\n";

	return 0;
}