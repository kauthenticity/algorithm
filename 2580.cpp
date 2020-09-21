#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int sudoku[9][9];
int ans[9][9];
int visited[10] = { 0, };
bool flag = false;

vector<pair<int, int>> zeros;

pair<int, int> find_zero_pos() {
	pair<int, int> temp;
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			if (sudoku[i][j] == 0) {
				temp.first = i;
				temp.second = j;

				return temp;
			}
		}
	}
	temp.first = temp.second = -1;

	return temp;
}

bool check_horizontal(int x, int y) {
	for (int i = 0; i < 9; i++) {
		visited[sudoku[x][i]]++;
	}

	for (int i = 1; i <= 9; i++) {
		if (visited[i] > 1) {
			memset(visited, 0, sizeof(visited));
			return false;
		}
	}

	memset(visited, 0, sizeof(visited));
	return true;
}
bool check_vertical(int x, int y) {
	for (int i = 0; i < 9; i++) {
		visited[sudoku[i][y]]++;
	}

	for (int i = 1; i <= 9; i++) {
		if (visited[i] > 1) {
			memset(visited, 0, sizeof(visited));
			return false;
		}
	}

	memset(visited, 0, sizeof(visited));
	return true;
}

bool check_box(int x, int y) {
	int a = (x / 3) * 3;
	int b = (y / 3) * 3;

	for (int i = a; i < a + 3; i++) {
		for (int j = b; j < b + 3; j++) {
			visited[sudoku[i][j]]++;
		}
	}

	for (int i = 1; i <= 9; i++) {
		if (visited[i] > 1) {
			memset(visited, 0, sizeof(visited));
			return false;
		}
	}

	memset(visited, 0, sizeof(visited));
	return true;
}

void go(int x, int y) {
	if (!flag) {
		for (int i = 1; i <= 9; i++) {
			int prev = sudoku[x][y];
			sudoku[x][y] = i;

			if (check_horizontal(x, y) && check_vertical(x, y) && check_box(x, y)) {
				pair<int, int> temp = find_zero_pos();

				if (temp.first == -1) {
					if (ans[0][0] == 0) {
						for (int k = 0; k < 9; k++) {
							for (int j = 0; j < 9; j++) {
								ans[k][j] = sudoku[k][j];
								flag = true;
							}
						}
					}
					return;
				}

				go(temp.first, temp.second);
			}
			sudoku[x][y] = prev;
		}
	}
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> sudoku[i][j];
			ans[i][j] = 0;
		}
	}

	pair<int, int> temp = find_zero_pos();
	go(temp.first, temp.second);

	for (int k = 0; k < 9; k++) {
		for (int j = 0; j < 9; j++) {
			cout << ans[k][j] << " ";
		}
		cout << "\n";
	}
	return 0;
}