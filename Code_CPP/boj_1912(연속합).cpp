#include <cstdio>
#include <algorithm>

int main() {
	int n;
	int arr[100000];
	int dp[100000] = { 0, };
	
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	dp[0] = arr[0];
	for (int i = 1; i < n; i++) {
		dp[i] = std::max(dp[i - 1] + arr[i], arr[i]);
	}
	printf("%d", *std::max_element(dp, dp+n));
	return 0;
}