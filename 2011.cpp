#include <iostream>
#include <string>

using namespace std;

#define A 1
#define J 10
#define Z 26

unsigned long long int dp[5001] = {0, };

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	string code;
	int temp;
	
	cin >> code;
	code.insert(0, "0");
	int n = code.length();

	if (code[1] == '0') {
		cout << 0 << "\n";
		return 0;
	}


	dp[0] = 1;
	dp[1] = 1;
	
 	for (int i = 2; i < n; i++) {
		dp[i] = dp[i - 1]; // �켱 ���� �� + ���� ����
		temp = (code[i - 1]-'0') * 10 + (code[i]-'0');
		if (code[i] == '0') { // ���� �ڵ尡 0�� ���
			if (temp > Z || temp < A) { // temp�� 0, 30, 40�� ����̹Ƿ� �߸��� �ڵ�
				cout << 0 << "\n";
				return 0;
			}
			//if (i ==n-1) {
			if(temp >= J && temp <= Z){
				dp[i] = dp[i - 2];
			}
		}
		else { // ���� �ڵ尡 0�� �ƴ� ���
			if (temp >= J && temp <= Z) {
				dp[i] = (dp[i] + dp[i - 2])%1000000;
			}
		}
	}
		

	cout << dp[n-1] % 1000000 << "\n";
	return 0;
}
