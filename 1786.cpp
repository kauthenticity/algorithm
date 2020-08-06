#include <iostream>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int failure[1000001];
int res[1000001];
char t[1000001], p[1000001];

void fail(char* t, char* p, int lenp) {
	int i;

	failure[0] = -1;

	for (int j = 1; j < lenp; j++) {
		i = failure[j - 1];

		while ((p[j] != p[i + 1]) && (i >= 0)) {
			i = failure[i];
		}

		if (p[j] == p[i + 1]) {
			failure[j] = i + 1;
		}
		else failure[j] = -1;
	}
}

void pmatch(char* t, char* p, int lens, int lenp, int& res_size) {
	int i = 0, j = 0;

	for (i = 0; i < lens; i++) {
		while (j > 0 && t[i] != p[j]) {
			j = failure[j - 1] + 1;
		}

		if (t[i] == p[j]) {
			j++;

			if (j == lenp) {
				res[res_size++] = i - lenp + 2;
				j = failure[j - 1] + 1;
			}
		}
	}
}


int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int res_size = 0;

	cin.getline(t, 1000001);
	cin.getline(p, 1000001);

	int lens = strlen(t);
	int lenp = strlen(p);

	fail(t, p, lenp);
	pmatch(t, p, lens, lenp, res_size);

	cout << res_size << "\n";

	for (int i = 0; i<res_size; i++) {
		cout << res[i] << "\n";
	}

	return 0;
}
