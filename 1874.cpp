#include <iostream>
#include <stack>

using namespace std;

#define PUSH 1
#define POP -1
int n;
int arr[100001];
int push_pop[200002];
stack <int> s;

bool go() {
	int i = 0, j = 0; // i : index of the given array, j : index of the push_pop array
	int top = 1;

	s.push(1);
	push_pop[j++] = PUSH;
	while (i < n) {
		if (s.empty()) { 
			s.push(++top);
			push_pop[j++] = PUSH;
		}
		else if (arr[i] > s.top()) {
			s.push(++top);
			push_pop[j++] = PUSH;
		}
		else if (arr[i] == s.top()) {
			s.pop();
			push_pop[j++] = POP;
			i++;
		}
		else {
			return false;
		}
	}
	return true;
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	if (go()) {
		for (int i = 0; i < 2 * n; i++) {
			if (push_pop[i] == PUSH) {
				cout << "+\n";
			}
			else {
				cout << "-\n";
			}
		}
	}
	else {
		cout << "NO\n";
	}

	return 0;
}