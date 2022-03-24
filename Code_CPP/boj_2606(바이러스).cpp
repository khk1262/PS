#include <iostream>
#include <queue>
#include <string.h>

using namespace std;

int bfs(int** g, bool* visit, int n, int v) {
	int comp = 0;
	queue<int> q;

	q.push(v);
	visit[v] = true;

	while (!q.empty()) {
		v = q.front();
		q.pop();

		for (int i = 1; i <= n; i++) {
			if (g[v][i] == 1 && !visit[i]) {
				q.push(i);
				visit[i] = true;
				comp++;
			}
		}
	}
	return comp;
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, m;

	cin >> n;
	cin >> m;

	int** graph = new int* [n + 1];
	bool* visited = new bool[n + 1];
	memset(visited, false, sizeof(bool) * (n + 1));

	for (int i = 0; i <= n; i++) {
		graph[i] = new int[n + 1];
		memset(graph[i], 0, sizeof(int) * (n + 1));
	}

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		graph[a][b] = 1;
		graph[b][a] = 1;
	}

	cout << bfs(graph, visited, n, 1) << '\n';
}