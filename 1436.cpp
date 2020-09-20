#include <iostream>
#include <string>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	int n, num = 666, i=0;
	string str;
	cin >> n;

	while (i < n) {
		str = to_string(num);

		if (str.find("666") != string::npos) {
			i++;
		}
		num++;
	}

	cout << str << "\n";

	return 0;
}