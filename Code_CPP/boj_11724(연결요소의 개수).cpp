#include <iostream>
#include <queue>
#include <string.h>

using namespace std;

void bfs(int** g, bool*& visit, int n, int v) {

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
			}
		}
	}
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m, cnt = 0;
	cin >> n >> m;

	int** arr2d = new int* [n + 1];

	for (int i = 0; i <= n; i++) {
		arr2d[i] = new int[n + 1];
		memset(arr2d[i], 0, sizeof(int) * (n + 1));
	}

	bool* visited = new bool[n + 1];

	memset(visited, false, sizeof(bool) * (n + 1));

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		arr2d[a][b] = 1;
		arr2d[b][a] = 1;
	}

	for (int i = 1; i <= n; i++) {
		if (!visited[i]) {
			bfs(arr2d, visited, n, i);
			cnt++;
		}
	}

	cout << cnt << endl;
}