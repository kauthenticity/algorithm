#include <iostream>
#include <algorithm>

using namespace std;

bool comp(const int a, const int b) {
	return a > b;
}

int arr[1000000];

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n;
	

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	sort(arr, arr + n, comp);

	for (int i = 0; i < n; i++) {
		cout << arr[i] << "\n";
	}

	return 0;
}
