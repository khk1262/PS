#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>

using namespace std;

int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { -1, 1, 0, 0 };

void bfs(vector<vector<char>>& g, int n, char type, int r, int c) {
	queue<pair<int, int>> q;

	q.push(make_pair(r, c));
	g[r][c] = 'N';

	while (!q.empty()) {
		r = q.front().first;
		c = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nr = r + dy[i];
			int nc = c + dx[i];

			if ((nr >= 0 && nr < n) && (nc >= 0 && nc < n)) {
				if (g[nr][nc] == type) {
					q.push(make_pair(nr, nc));
					g[nr][nc] = 'N';
				}
			}
		}
	}
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	vector<vector<char>> graph;
	vector<vector<char>> graph_not;

	cin >> n;

	graph.resize(n, vector<char>(n));
	graph_not.resize(n, vector<char>(n));

	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < n; j++) {
			if (s[j] == 'R' || s[j] == 'G') {
				graph_not[i][j] = 'R';
			}
			else {
				graph_not[i][j] = 'B';
			}
			graph[i][j] = s[j];
		}
	}

	int cnt = 0;
	int cnt_not = 0;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (graph[i][j] == 'R') {
				bfs(graph, n, 'R', i, j);
				cnt++;
			}
			else if (graph[i][j] == 'G') {
				bfs(graph, n, 'G', i, j);
				cnt++;
			}
			else if (graph[i][j] == 'B') {
				bfs(graph, n, 'B', i, j);
				cnt++;
			}

			if (graph_not[i][j] == 'R') {
				bfs(graph_not, n, 'R', i, j);
				cnt_not++;
			}
			else if (graph_not[i][j] == 'B') {
				bfs(graph_not, n, 'B', i, j);
				cnt_not++;
			}
		}
	}
	cout << cnt << " " << cnt_not << '\n';
}