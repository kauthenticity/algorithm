#include <iostream>

using namespace std;

#define min(x, y) ((x)<(y)?(x):(y))
#define MAX 801
#define INF 2100000000

int V, E;
int v1, v2;
int graph[MAX][MAX];

void floyd() {
	for (int k = 1; k <= V; k++) {
		for (int i = 1; i <= V; i++) {
			for (int j = 1; j <= V; j++) {
				if (graph[i][k] == INF || graph[k][j] == INF) {
					continue;
				}

				if (graph[i][k] + graph[k][j] < graph[i][j]) {
					graph[i][j] = graph[i][k] + graph[k][j];
				}
			}
		}
	}
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int u, v, w, path1, path2, min_dist;

	cin >> V >> E;

	for (int i = 1; i <= V; i++) {
		for (int j = 1; j <= V; j++) {
			if (i == j) {
				graph[i][j] = 0;
			}
			else {
				graph[i][j] = INF;
			}
		}
	}

	for (int i = 0; i < E; i++) {
		cin >> u >> v >> w;
		graph[u][v] = w;
		graph[v][u] = w;
	}

	cin >> v1 >> v2;

	floyd();

	if (graph[1][v1] == INF || graph[v1][v2] == INF || graph[v2][V] == INF || graph[1][v2] == INF || graph[v1][V] == INF) {
		cout << "-1";
	}
	else {

		path1 = graph[1][v1] + graph[v1][v2] + graph[v2][V];
		path2 = graph[1][v2] + graph[v2][v1] + graph[v1][V];

		min_dist = min(path1, path2);
		
		cout << min_dist << "\n";
	}

	return 0;
}