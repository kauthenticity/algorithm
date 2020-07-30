#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

short int books[1001] = {false, };

bool comp(const pair<int, int>& a, const pair<int, int>& b) {
	if (a.second != b.second) {
		return a.second < b.second;
	}
	return a.first < b.first;
}

int count_students(vector<pair <int, int>> v, int n, int m) {
	int cnt = 0;

	for (int i = 0; i < m; i++) {
		for (int j = v[i].first; j <= v[i].second; j++) {
			if (!books[j]) {
				books[j] = true;
				cnt++;
				break;
			}
		}
	}
	return cnt; 
}

void clear_books() {
	for (int i = 0; i < 1001; i++) {
		books[i] = false;
	}
}
int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int t, n, m, a, b;

	// t : # of test cases
	// n : maximum book number
	// m : # of students
	// a, b : book numberes students submitted

	cin >> t;

	for (int i = 0; i < t; i++) {
		vector <pair <int, int>> v;
		cin >> n >> m;

		for (int j = 0; j < m; j++) {
			cin >> a >> b;
			v.push_back(pair<int, int>(a, b));
		}

		sort(v.begin(), v.end(), comp);

		cout << count_students(v, n, m) << "\n";
		clear_books();
	}

	return 0;
}
