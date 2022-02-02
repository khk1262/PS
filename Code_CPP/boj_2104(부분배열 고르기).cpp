#include <cstdio>
#include <algorithm>

using namespace std;

int N;
long long H[100000];

long long solve2(int left, int right) {
	if (left == right) return H[left] * H[left];

	int mid = (left + right) / 2;
	long long ret = max(solve2(left, mid), solve2(mid + 1, right));

	int lo = mid, hi = mid + 1;

	long long mul = min(H[lo], H[hi]);
	long long total = H[lo] + H[hi];

	ret = max(ret, mul * total);

	while (left < lo || hi < right) {
		if (hi < right && (lo == left || H[lo - 1] < H[hi + 1])) {
			++hi;
			mul = min(mul, H[hi]);
			total += H[hi];
		}
		else {
			--lo;
			mul = min(mul, H[lo]);
			total += H[lo];
		}
		ret = max(ret, mul * total);
	}
	return ret;
}



int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d", &H[i]);
	printf("%lld", solve2(0, N-1));
}