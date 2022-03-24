#include <iostream>
#include <queue>
#include <string.h>
#include <utility>

using namespace std;

int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { -1, 1, 0, 0 };

int bfs(int** g, int n, int m, int r, int c) {
	if (g[r][c] == 0) return 0;

	int comp = 1;
	queue<pair<int, int>> q;
	q.push(make_pair(r, c));

	g[r][c] = 0;

	while (!q.empty()) {

		r = q.front().first;
		c = q.front().second;

		q.pop();

		for (int i = 0; i < 4; i++) {
			int nr = r + dy[i];
			int nc = c + dx[i];

			if ((nr >= 1 && nr <= n) && (nc >= 1 && nc <= m)) {
				if (g[nr][nc] == 1) {
					g[nr][nc] = 0;
					q.push(make_pair(nr, nc));
					comp++;
				}
			}
		}
	}
	return comp;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m, k;


	cin >> n >> m >> k;

	int** arr2d = new int* [n + 1];
	for (int i = 0; i <= n; i++) {
		arr2d[i] = new int[m + 1];
		memset(arr2d[i], 0, sizeof(int) * (m + 1));
	}

	for (int i = 0; i < k; i++) {
		int r, c;
		cin >> r >> c;
		arr2d[r][c] = 1;
	}

	int max_val = -1;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (arr2d[i][j] == 1) {
				int temp = bfs(arr2d, n, m, i, j);
				max_val = max_val > temp ? max_val : temp;
			}
		}
	}

	cout << max_val << endl;
}