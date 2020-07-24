#include <iostream>

using namespace std;

unsigned short int arr[10001] = {0, };
int n;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int t, max = 0;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> t;
		arr[t]++;
		if (max < t) {
			max = t;
		}
	}
	for (int i = 0; i <= max; i++) {
		for (int j = 0; j < arr[i]; j++) {
			cout << i << "\n";
		}
	}

	return 0;
}