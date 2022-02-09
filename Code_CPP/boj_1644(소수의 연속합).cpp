#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>

#define MAX 4000000

int N;
int prime[MAX];

std::vector<int> v;

void make_prime() {
	std::fill(prime, prime + MAX, 1);

	prime[0] = 0, prime[1] = 0;
	for (int i = 2; i < MAX; i++) {
		if (prime[i]) v.push_back(i);
		for (int j = i * 2; j < MAX; j += i) {
			if (prime[j]) prime[j] = 0;
		}
	}
}

int main() {
	make_prime();

	scanf("%d", &N);

	int low = 0, high = 0, total = 0;
	int cnt = 0;
	int M = v.size();

	while (1) {
		if (total >= N) total -= v[low++];
		else if (high == M) break;
		else total += v[high++];
		if (total == N) cnt++;
	}

	printf("%d", cnt);

	return 0;
}