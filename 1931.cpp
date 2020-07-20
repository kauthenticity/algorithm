#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

bool comp(pair <int, int>a, pair <int, int>b) {
	return a.second < b.second;
}

int countMeeting(vector <pair<int, int>>v) {
	int curEnd = v[0].second;
	int cnt = 1;

	for (int i = 1; i < v.size(); i++) {
		if (v[i].first >= curEnd) {
			curEnd = v[i].second;
			cnt++;
		}
	}

	return cnt;
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n, start, end;
	vector <pair<int, int>> v;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> start >> end;
		v.push_back(pair<int, int>(start, end));
	}

	sort(v.begin(), v.end());
	sort(v.begin(), v.end(), comp);

	int res = countMeeting(v);

	cout << res << endl;

	return 0;
}