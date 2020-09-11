#include <iostream>
#include <vector>
#include <tuple>
#include <queue>
#include <functional>

using namespace std;

#define MAX_VERTEX 20001
#define MAX_EDGE 300001
#define INF 2100000000

typedef pair<int, int> P;

int V, E, K;

vector<P> graph[MAX_VERTEX];
priority_queue<P, vector<P>, greater<P>> minheap;
vector<int> dist;

void dijkstra() {
	int cur_vertex, length;
	dist.push_back(INF);
	for (int i = 1; i <= V; i++) {
		dist.push_back(INF);
	}
	//distance, found array initialization
	
	dist[K] = 0; // distance to starting ponit is 0
	minheap.push(P(0, K));

	while (!minheap.empty()) {
		P front = minheap.top(); minheap.pop();
		length = front.first; cur_vertex = front.second;

		for (int i = 0; i < graph[cur_vertex].size(); i++) { 
			// vertex adjacent to curent vertex
			int adj_vertex = graph[cur_vertex][i].first;
			int cost = graph[cur_vertex][i].second;

			if (length + cost < dist[adj_vertex]) {
				dist[adj_vertex] = length+cost;
				minheap.push(P(length+cost, adj_vertex));
			}
		}
	}
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	int u, v, w;

	cin >> V >> E >> K;

	for (int i = 0; i < E; i++) {
		cin >> u >> v >> w;

		graph[u].push_back(P(v, w));
	}

	dijkstra();


	for (int i = 1; i <= V; i++) {
		if (dist[i] == INF) {
			cout << "INF\n";
		}
		else {
			cout << dist[i] << "\n";
		}
	}
	
	return 0;
}