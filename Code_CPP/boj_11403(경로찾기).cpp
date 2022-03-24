#include <iostream>
#include <queue>
#include <string.h>
#include <string>

using namespace std;

void bfs(int** graph, bool* visit, int n, int v, int*& temp) {
	queue<int> q;
	q.push(v);

	while (!q.empty()) {
		int nv = q.front();
		q.pop();

		for (int i = 0; i < n; i++) {
			if (graph[nv][i] == 1 && !visit[i]) {
				q.push(i);
				visit[i] = true;
				temp[i] = 1;
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int n;

	cin >> n;

	int** arr2d = new int* [n];
	int* temp = new int[n];
	bool* visited = new bool[n];
	for (int i = 0; i < n; i++) {
		arr2d[i] = new int[n];
		memset(arr2d[i], 0, sizeof(int) * n);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr2d[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		memset(visited, false, sizeof(bool) * n);
		memset(temp, 0, sizeof(int) * n);

		bfs(arr2d, visited, n, i, temp);
		for (int j = 0; j < n; j++)
			cout << temp[j] << " ";
		cout << '\n';
	}
}