#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int N, H[100000];

int solve(int left, int right) {
	if (left == right) return H[left];

	int mid = (left + right) / 2;
	int ret = max(solve(left, mid), solve(mid + 1, right));

	int lo = mid, hi = mid + 1;
	int height = min(H[lo], H[hi]);

	ret = max(ret, height * 2);

	while (left < lo || hi < right) {
		if (hi < right && (lo == left || H[lo - 1] < H[hi + 1])) {
			++hi;
			height = min(height, H[hi]);
		}
		else {
			--lo;
			height = min(height, H[lo]);
		}
		ret = max(ret, height * (hi - lo + 1));
	}
	return ret;
}


int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &H[i]);
	}
	printf("%d", solve(0, N-1));
}