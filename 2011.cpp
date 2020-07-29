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
		dp[i] = dp[i - 1]; // 우선 전에 거 + 현재 문자
		temp = (code[i - 1]-'0') * 10 + (code[i]-'0');
		if (code[i] == '0') { // 현재 코드가 0인 경우
			if (temp > Z || temp < A) { // temp가 0, 30, 40인 경우이므로 잘못된 코드
				cout << 0 << "\n";
				return 0;
			}
			//if (i ==n-1) {
			if(temp >= J && temp <= Z){
				dp[i] = dp[i - 2];
			}
		}
		else { // 현재 코드가 0이 아닌 경우
			if (temp >= J && temp <= Z) {
				dp[i] = (dp[i] + dp[i - 2])%1000000;
			}
		}
	}
		

	cout << dp[n-1] % 1000000 << "\n";
	return 0;
}
