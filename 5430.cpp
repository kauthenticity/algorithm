#include <iostream>
#include <queue>
#include <string>

using namespace std;

bool rflag = false;

void get_deque(deque<int>& dq, int dq_size) {
	char c;
	int val;
	cin >> c;
	if (dq_size == 0) {
		cin >> c;
		return;
	}
	for (int i = 0; i < dq_size; i++) {
		cin >> val >> c;
		dq.push_back(val);
	}
}

bool process_command(string command, deque<int> &dq) {
	int i = 0;
	int temp;
	int strlen = command.length();
	while (i < strlen) {
		if (command[i] == 'R') {
			rflag = (rflag == false ? true : false);
		}
		else {
			if (dq.empty()) {
				return false;
			}

			if (rflag) {
				dq.pop_back();
			}
			else {
				dq.pop_front();
			}
		}
		i++;
	}
	return true;
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int t, dq_size, val, j;
	string command;

	cin >> t;

	for (int i = 0; i < t; i++) {
		deque<int> dq;
		rflag = false;
		cin >> command >> dq_size;
		get_deque(dq, dq_size);
		if (process_command(command, dq)) {
			cout << "[";
			int size = dq.size();
			if (rflag) {
				for (j = size-1; j > 0; j--) {
					cout << dq[j] << ",";
				}
				if (!dq.empty()) {
					cout << dq[0];
				}
			}
			else {
				for (j = 0; j < size-1; j++) {
					cout << dq[j] << ",";
				}
				if (!dq.empty()) {
					cout << dq[dq.size() - 1];
				}
			}
			cout << "]\n";
		}
		else {
			cout << "error\n";
		}
	}
	return 0;
}