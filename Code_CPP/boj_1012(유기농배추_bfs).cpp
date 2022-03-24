#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { -1, 1, 0, 0 };

bool bfs(int** map, int w, int h, int x, int y) {
	queue<pair<int, int>> q;
	q.push(make_pair(y, x));
	map[y][x] = 0;

	while (!q.empty()) {
		int x = q.front().second;
		int y = q.front().first;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if ((ny >= 0 && ny < h) && (nx >= 0 && nx < w)) {
				if (map[ny][nx] == 1) {
					map[ny][nx] = 0;
					q.push(make_pair(ny, nx));
				}
			}
		}
	}
	return true;
}

int solve(int** arr2d, int width, int height) {

	int total = 0;
	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {
			if (arr2d[i][j] == 1) {
				bfs(arr2d, width, height, j, i);
				total++;
			}
		}
	}
	return total;
}


int main() {
	int t, m, n, k;
	int** arr2d;
	cin >> t;
	while (t--) {
		cin >> m >> n >> k;

		arr2d = new int* [n];
		for (int i = 0; i < n; i++)
			arr2d[i] = new int[m]();

		for (int t = 0; t < k; t++) {
			int a, b;
			cin >> a >> b;
			arr2d[b][a] = 1;
		}

		cout << solve(arr2d, m, n) << endl;
		for (int i = 0; i < n; i++)
			delete[] arr2d[i];
		delete[] arr2d;
	}

}