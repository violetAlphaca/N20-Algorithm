#include <algorithm>
#include <iostream>
using namespace std;

int maleCnt, femaleCnt, maleValue[1010], femaleValue[1010], dp[1010][1010];

int abs(int a, int b) { return a > b ? a - b : b - a; }

int main(void) {
  cin >> maleCnt >> femaleCnt;
  for (int i = 1; i <= maleCnt; i++) scanf(" %d", &maleValue[i]);
  for (int i = 1; i <= femaleCnt; i++) scanf(" %d", &femaleValue[i]);

  sort(maleValue + 1, maleValue + maleCnt + 1);
  sort(femaleValue + 1, femaleValue + femaleCnt + 1);

  for (int maleIdx = 1; maleIdx <= maleCnt; maleIdx++) {
    for (int femaleIdx = 1; femaleIdx <= femaleCnt; femaleIdx++) {
      if (maleIdx == femaleIdx) {
        dp[maleIdx][femaleIdx] =
            dp[maleIdx - 1][femaleIdx - 1] +
            abs(maleValue[maleIdx], femaleValue[femaleIdx]);
      } else if (maleIdx > femaleIdx) {
        dp[maleIdx][femaleIdx] =
            min(dp[maleIdx - 1][femaleIdx],
                dp[maleIdx - 1][femaleIdx - 1] +
                    abs(maleValue[maleIdx], femaleValue[femaleIdx]));
      } else if (maleIdx < femaleIdx) {
        dp[maleIdx][femaleIdx] =
            min(dp[maleIdx][femaleIdx - 1],
                dp[maleIdx - 1][femaleIdx - 1] +
                    abs(maleValue[maleIdx], femaleValue[femaleIdx]));
      }
    }
  }

  cout << dp[maleCnt][femaleCnt] << endl;

  return 0;
}

/*
3 3
10 20 100
1 2 3


3 2
1 99 100
98 99
*/