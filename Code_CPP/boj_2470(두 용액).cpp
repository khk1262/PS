#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <algorithm>
#include <cmath>

using LLONG = long long;

int N;
LLONG arr[100000];

int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%lld", &arr[i]);
	}

	std::sort(arr, arr + N);


	LLONG min_val = (LLONG)1e10;
	LLONG left = 0, right = 0;

	int low = 0, high = N-1;
	LLONG sum = arr[low] + arr[high];

	while (1) {
		if (std::abs(sum) > min_val) {
			if (sum > 0) {
				sum -= arr[high];
				sum += arr[--high];
			}
			else {
				sum -= arr[low];
				sum += arr[++low];
			}
		}
		else {
			min_val = std::abs(sum);
			left = arr[low], right = arr[high];

			if (sum > 0) {
				sum -= arr[high];
				sum += arr[--high];
			}
			else {
				sum -= arr[low];
				sum += arr[++low];
			}
		}

		if (low >= high) {
			break;
		}
	}

	printf("%lld %lld\n", left, right);

	return 0;
}