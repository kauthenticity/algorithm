#include <iostream>

using namespace std;

#define min(x, y) ((x)<(y)?(x):(y))
#define MAX 101
#define INF 2100000000

int V, E;
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
	int u, v, w;

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
		graph[u][v] = min(graph[u][v], w);
	}

	floyd();

	for (int i = 1; i <= V; i++) {
		for (int j = 1; j <= V; j++) {
			if (!graph[i][j]) {
				cout << "0 ";
			}
			else {
				cout << graph[i][j] << " ";
			}
		}
		cout << "\n";
	}

	return 0;
}