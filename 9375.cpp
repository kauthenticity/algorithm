#include <iostream>
#include <map>
#include <cstring>

using namespace std;

#define MAX 30


int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int t, n;
	string name, type;

	cin >> t;

	for (int i = 0; i < t; i++) {
		map<string, int> m;
		map<string, int>::iterator it;
		cin >> n;

		for (int j = 0; j < n; j++) {
			cin >> name >> type;
			
			it = m.find(type);
			if (it == m.end()) {
				m[type] = 1;
			}
			else {
				m[type]++;
			}
		}

		int res = 1;

		for (it = m.begin(); it != m.end(); it++) {
			res *= (it->second) + 1;
		}

		cout << res - 1 << "\n";
	}

	return 0;
}
