#include <iostream>
#include <algorithm>

using namespace std;
int n;
int k;
int* arr;
bool flag = false;
void merge(int h, int m, int* u, int* v, int* s) {
	int i, j, k;
	i = 0; j = 0; k = 0;

	while (i < h && j < m) {
		if (u[i] < v[j]) {
			s[k++] = u[i++];
		}
		else {
			s[k++] = v[j++];
		}
	}
	if (i >= h) {
		for (int l = j; l < m; j++) {
			s[k++] = v[l];
		}
	}
	else {
		for (int l = i; l < h; j++) {
			s[k++] = u[l];
		}
	}
}
void mergesort(int n, int *arr) {
	if (!flag) {
		if (n > 1) {
			const int h = n / 2, m = n - h;
			int* u = new int[h];
			int* v = new int[m];
			for (int i = 0; i < h; i++) {
				u[i] = arr[i];
			}
			for (int i = h; i < n; i++) {
				v[i - h] = arr[i];
			}
			mergesort(h, u);
			mergesort(m, v);
			merge(h, m, u, v, arr);

			if (k < m) {
				flag = true;
			}
		}
	}
}
int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n >> k;

	arr = new int[n];

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	sort(arr, arr + n);

	cout << arr[k - 1] << "\n";

	return 0;
}