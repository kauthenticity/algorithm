#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main(void) {
	string sent;

	while (1) {
		bool flag = false;
		stack <char>s;
		getline(cin, sent);

		if (sent[0] == '.') {
			break;
		}

		for (int i = 0; i < sent.length(); i++) {
			if (sent[i] == '(' || sent[i] == '[') {
				s.push(sent[i]);
			}
			else if (sent[i] == ')') {
				if (s.empty()) {
					flag = true;
					break;
				}
				if (s.top() != '(') {
					bool flag = true;
					break;
				}
				s.pop();
			}
			else if (sent[i] == ']') {
				if (s.empty()) {
					flag = true;
					break;
				}
				if (s.top() != '[') {
					bool flag = true;
					break;
				}
				s.pop();
			}
		}

		if (s.empty() && flag==false) {
			cout << "yes" << "\n";
		}
		else {
			cout << "no" << "\n";
		}
	}

	return 0;
}