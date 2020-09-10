#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define MAX 1001
#define INF 2100000000
#define min(x, y) ((x)<(y) ? (x):(y))
int n, m;
int x_dir[4];
int y_dir[4];
int dist[MAX][MAX] = {INF, };
bool maze[MAX][MAX];

queue<pair<int, int>> q;
queue<pair<int, int>> newq;

bool is_inside(int x, int y) {
	return (x >= 1 && x <= n && y >= 1 && y <= m);
}

void go() {
	int x, y, newx, newy;
	q.push(pair<int, int>(1, 1));
	dist[1][1] = 1;

	while (!q.empty()) {
		pair<int, int> front = q.front();
		q.pop();

		x = front.first;
		y = front.second;

		for (int i = 0; i < 4; i++) {
			newx = x + x_dir[i];
			newy = y + y_dir[i];

			if (is_inside(newx, newy) && dist[newx][newy] > dist[x][y] + 1) { //아직 방문하지 않았으며 범위 내에 있는 경우
				if(maze[newx][newy]){ //wall
					newq.push(pair<int, int>(newx, newy));
				}
				else { // path
					q.push(pair<int, int>(newx, newy));
				}
				dist[newx][newy] = dist[x][y] + 1;
			}
		}
	}

	while (!newq.empty()) {
		pair<int, int> front = newq.front();
		newq.pop();

		x = front.first;
		y = front.second;
		for (int i = 0; i < 4; i++) {
			newx = x + x_dir[i];
			newy = y + y_dir[i];

			if (is_inside(newx, newy) && dist[newx][newy] > dist[x][y] + 1 && !maze[newx][newy]) {
				newq.push(pair<int, int>(newx, newy));
				dist[newx][newy] = dist[x][y] + 1;
			}
		}
	}
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	string str;
	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		cin >> str;
		for (int j = 1; j<=str.length(); j++) {
			maze[i][j] = str[j-1] - '0';
			dist[i][j] = INF;
		}
	} // input
	
	x_dir[0] = -1; x_dir[1] = 0; x_dir[2] = 1; x_dir[3] = 0;
	y_dir[0] = 0; y_dir[1] = 1; y_dir[2] = 0;  y_dir[3] = -1;
	//direction initialization

	go();

	if (dist[n][m] == INF) {
		cout << "-1\n";
	}
	else {
		cout << dist[n][m] << "\n";
	}
	

	return 0;
}