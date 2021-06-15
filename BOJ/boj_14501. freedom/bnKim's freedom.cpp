#include <stdio.h>
#include <stdlib.h>
#include <queue>
#include <memory.h>
#include <vector>
using namespace std;

//백준 14501. 퇴사

vector <int> T;
vector<int> P;
vector<int> incomes;
int maxIncome = 0;
int getIncome(int start, int current);

int main() {
	int N = 0;
	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		int t = 0, p = 0;
		scanf("%d %d", &t, &p);
		T.push_back(t);
		P.push_back(p);
	}

	getIncome(0, 0); //start
	printf("%d", maxIncome);

	getchar();
	getchar();
	return 0;
}

//재귀, 브루트 포스
int getIncome(int day, int income) {
	
	//아래의 두 if문에서 퇴사일 범위를 벗어난 것은 걸러짐
	if (day > T.size()) {
		return -1;			//퇴사일을 넘어서면 -1 리턴
	}
	else if (day == T.size()) {
		return income;		//퇴사일까지 일했으면 income 리턴
	}

	int no = getIncome(day + 1, income); // 현재 day에 상담하지 않는경우의 income합계 리턴
	int yes = getIncome(day + T.at(day), income + P.at(day)); //현재 day에 상담하는 경우의 income합계 리턴

	int temp = max(no, yes);
	income = max(income, temp);
	if (income > maxIncome) maxIncome = income;

	return income;
}
