#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	int n, val;
	string str;
	deque<int> dq;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> str;

		if (str.compare("push_front") == 0) {
			cin >> val;
			dq.push_front(val);
		}
		else if (str.compare("push_back") == 0) {
			cin >> val;
			dq.push_back(val);
		}
		else if (str.compare("pop_front") == 0) {
			if (!dq.empty()) {
				cout << dq.front() << "\n";
				dq.pop_front();
			}
			else{
				cout << "-1\n";
			}
		}
		else if (str.compare("pop_back") == 0) {
			if (!dq.empty()) {
				cout << dq.back() << "\n";
				dq.pop_back();
			}
			else {
				cout << "-1\n";
			}
		}
		else if (str.compare("size") == 0) {
			cout << dq.size() << "\n";
		}
		else if (str.compare("empty") == 0) {
			cout << dq.empty() << "\n";
		}
		else if (str.compare("front") == 0) {
			if (!dq.empty()) {
				cout << dq.front() << "\n";
			}
			else {
				cout << "-1\n";
			}
		}
		else if (str.compare("back") == 0) {
			if(!dq.empty()) {
				cout << dq.back() << "\n";
			}
			else {
				cout << "-1\n";
			}
		}
	}
	return 0;
}