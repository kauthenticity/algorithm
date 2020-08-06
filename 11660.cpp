#include <iostream>

using namespace std;

long long int arr[1024][1024];
long long int memo[1024][1024];
int n;

void make_memo() {
	memo[0][0] = arr[0][0];

	for (int i = 1; i < n; i++) {
		memo[i][0] = memo[i - 1][0] + arr[i][0];
	}
	for (int j = 1; j < n; j++) {
		memo[0][j] = memo[0][j-1] + arr[0][j];
	}
	for (int i = 1; i < n; i++) {
		for (int j = 1; j < n; j++) {
			memo[i][j] = memo[i - 1][j] + memo[i][j - 1] - memo[i - 1][j - 1] + arr[i][j];
		}
	}
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int m, x1, x2, y1, y2;


	cin >> n >> m;
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
		}
	}

	make_memo();

	for (int i = 0; i < m; i++) {
		cin >> x1 >> y1 >> x2 >> y2;

		if (x1 == 1 || y1 == 1) {
			if (x1 == 1 && y1 == 1) {
				cout << memo[x2 - 1][y2 - 1] << "\n";
			}
			else if (x1 == 1) {
				cout << memo[x2 - 1][y2 - 1] - memo[x2 - 1][y1 - 2] << "\n";
			}
			else {
				cout << memo[x2 - 1][y2 - 1] - memo[x1 - 2][y2 - 1] << "\n";
			}
		}
		else {
			cout << memo[x2 - 1][y2 - 1] - memo[x1 - 2][y2 - 1] - memo[x2 - 1][y1 - 2] + memo[x1 - 2][y1 - 2] << "\n";
		}
	}

	return 0;
}
