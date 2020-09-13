#include <iostream>
#include <vector>

using namespace std;

#define min(x, y) ((x)<(y)?(x):(y))
#define MAX 501
#define INF 2100000000

int V, E;
long long dist[MAX] = {INF, };
int length[MAX][MAX];
bool flag = false;
vector<int> graph[MAX];
//graph[i][j] = v :  there exists edge from v to i


bool bellman_ford() {
	for (int i = 1; i <= V; i++) {
		dist[i] = length[1][i];
	}

	for (int k = 1; k <= V; k++) {
		for (int u = 1; u <= V; u++) {
			if (graph[u].empty()) {
				continue;
			}
			for (int j = 0; j < graph[u].size(); j++) {
				int i = graph[u][j];
				if (dist[i] == INF) {
					continue;
				}
				if (dist[u] > dist[i] + length[i][u]) {
					dist[u] = dist[i] + length[i][u];
					if (k == V) {
						return true;
					}
				}
			}
		}
	}

	return false;
}


int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int u, v, w;

	cin >> V >> E;

	for (int i = 1; i <= V; i++) {
		for (int j = 1; j <= V; j++) {
			if (i == j) {
				length[i][j] = 0;
			}
			else {
				length[i][j] = INF;
			}
		}
	}

	for (int i = 0; i < E; i++) {
		cin >> u >> v >> w;
		graph[v].push_back(u);
		length[u][v] = min(length[u][v], w);
	}

	//bellman_ford();
	if (bellman_ford()) {
		cout << "-1\n";
		return 0;
	}

	for (int i = 2; i <= V; i++) {
		if (dist[i] == INF) {
			cout << "-1\n";
		}
		else {
			cout << dist[i] << "\n";
		}
	}


	return 0;
}