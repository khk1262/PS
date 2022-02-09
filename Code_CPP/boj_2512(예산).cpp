#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <algorithm>

using namespace std;

int main() {

	int N, M;
	int budget[100001];
	int max_val = -1;

	scanf("%d", &N);

	for (int i = 0; i < N; ++i) {
		scanf("%d", &budget[i]);
		max_val = max(max_val, budget[i]);
	}
	scanf("%d", &M);

	int low = 0, high = max_val;
	int result = 0;

	while (low <= high) {
		int mid = (low + high) / 2;
		long long sum = 0;
		for (int i = 0; i < N; ++i) {
			if (budget[i] < mid) sum += budget[i];
			else sum += mid;
		}
		if (sum > M)
			high = mid - 1;
		else {
			low = mid + 1;
			result = mid;
		}
	}
	printf("%d", result);
}