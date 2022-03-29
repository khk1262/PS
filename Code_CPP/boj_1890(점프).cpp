#include <iostream>
#include <algorithm>

using namespace std;

int graph[100][100];
long long dp[100][100] = { 0, };
int n;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			cin >> graph[i][j];
	}

	dp[0][0] = 1;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (i == n - 1 && j == n - 1) break;
			if (graph[i][j] + j < n)
				dp[i][graph[i][j] + j] += dp[i][j];
			if (graph[i][j] + i < n)
				dp[graph[i][j] + i][j] += dp[i][j];
		}
	}
	cout << dp[n - 1][n - 1];
}