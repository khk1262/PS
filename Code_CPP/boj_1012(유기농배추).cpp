#include <iostream>

using namespace std;

int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { -1, 1, 0, 0 };

bool dfs(int** map, int w, int h, int x, int y) {
	int ny, nx;

	for (int i = 0; i < 4; i++) {
		ny = y + dy[i];
		nx = x + dx[i];

		if ((ny >= 0 && ny < h) && (nx >= 0 && nx < w)) {
			if (map[ny][nx] == 1) {
				map[ny][nx] = -1;
				if (dfs(map, w, h, nx, ny))
					return true;
			}
		}
	}
	return false;
}


int solve(int width, int height, int k) {
	int** arr2d = new int* [height];
	for (int i = 0; i < height; i++)
		arr2d[i] = new int[width];

	fill(&arr2d[0][0], &arr2d[height - 1][width], 0);// fill로 초기화
	int total = 0;

	for (int t = 0; t < k; t++) {
		int a, b;
		cin >> a >> b;
		arr2d[b][a] = 1;
	}

	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {
			if (arr2d[i][j] == 1) {
				dfs(arr2d, width, height, j, i);
				total++;
			}
		}
	}
	return total;
}


int main() {
	int t, m, n, k;
	cin >> t;
	while (t--) {
		cin >> m >> n >> k;
		cout << solve(m, n, k) << endl;
	}
}