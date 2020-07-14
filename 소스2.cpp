#include <iostream>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>

using namespace std;

int n;
pair <int, string> p;
vector <pair<int, string>> people_info;
void merge(int h, int m, vector <pair<int, string>> u, vector <pair<int, string>> v, vector <pair<int, string>> &s) {
	int i, j, k;

	i = 0, j = 0, k = 0;

	while(i < h && j < m) {
		if (u[i].first <= v[j].first) {
			s[k] = u[i]; i++;
		}
		else {
			s[k] = v[j]; j++;
		}
		k++;
	}

	if (i >= h) {
		for (int l = j; l < m; l++) {
			s[k++] = v[l];
		}
	}
	else {
		for (int l = i; l < h; l++) {
			s[k++] = u[l];
		}
	}
}
void mergesort(int n, vector <pair<int, string>> &s) {
	if (n > 1) {
		int h = n / 2, m = n - h; 
		vector <pair<int, string>> u, v;

		for (int i = 0; i < h; i++) {
			u.push_back(s[i]);
		}
		for (int i = h; i < n; i++) {
			v.push_back(s[i]);
		}
		mergesort(h, u);
		mergesort(m, v);
		merge(h, m, u, v, s);
	}
}
int main(void) {
	int age;
	string name;

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> age >> name;
		people_info.push_back(make_pair(age, name));
	}

	mergesort(n, people_info);

	for (int i = 0; i < n; i++)
		cout << people_info[i].first << " " << people_info[i].second << "\n";
	return 0;
}