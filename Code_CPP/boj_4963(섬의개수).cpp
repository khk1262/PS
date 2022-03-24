#include <iostream>
#include <queue>
#include <string.h>
#include <utility>

using namespace std;

int dy[8] = { -1, -1, -1, 0, 0, 1, 1, 1 };
int dx[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };


void bfs(int**& g, int w, int h, int r, int c) {
	queue<pair<int, int>> q;
	q.push(make_pair(r, c));
	g[r][c] = 0;

	while (!q.empty()) {
		r = q.front().first;
		c = q.front().second;
		q.pop();
		for (int i = 0; i < 8; i++) {
			int nr = r + dy[i];
			int nc = c + dx[i];

			if ((nr >= 0 && nr < h) && (nc >= 0 && nc < w)) {
				if (g[nr][nc] == 1) {
					q.push(make_pair(nr, nc));
					g[nr][nc] = 0;
				}
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int w, h;

	while (true) {
		int cnt = 0;
		cin >> w >> h;

		if (w == 0 && h == 0) break;

		int** graph = new int* [h];
		for (int i = 0; i < h; i++) {
			graph[i] = new int[w];
			memset(graph[i], 0, sizeof(int) * w);
		}

		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				cin >> graph[i][j];
			}
		}

		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (graph[i][j] == 1) {
					bfs(graph, w, h, i, j);
					cnt++;
				}
			}
		}
		cout << cnt << '\n';

		for (int i = 0; i < h; i++) {
			delete[] graph[i];
		}
		delete[] graph;

	}
}