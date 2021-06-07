#include <iostream>
#include <vector>

using namespace std;

typedef pair<int, int> pii;

int Map[9][9] = {0};
int Col[9] = {0};
int Row[9] = {0};
int Box[9] = {0};
vector<pii> cand;

void Check(int y, int x, int i) {
  int value = 1 << i;
  Row[y] ^= value;
  Col[x] ^= value;
  int index = (y / 3) * 3 + (x / 3);
  Box[index] ^= value;
}

void In() {
  int tmp;
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      cin >> tmp;
      Map[i][j] = tmp;
      Check(i, j, tmp);
      if (tmp == 0)
        cand.push_back(pii(i, j));
    }
  }
  cout << endl;
}

void Print() {
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      cout << Map[i][j] << " ";
    }
    cout << endl;
  }
}

bool IsValid(int y, int x, int i) {
  // Map[y][x]에 i를 넣을 수 있는가
  int value = 1 << i;
  int index = (y / 3) * 3 + (x / 3);
  return !((Row[y] & value) || (Col[x] & value) ||
         (Box[index] & value));
}

bool FindAns() {
  if (cand.empty()) {
    return true;
  }

  for (int i = 1; i < 10; i++) {
    int y = cand.back().first;
    int x = cand.back().second;
    if (IsValid(y, x, i)) {
      cand.pop_back();
      Map[y][x] = i;
      Check(y, x, i);
      if (FindAns()) {
        return true;
      } else {
        Map[y][x] = 0;
        Check(y, x, i); // Uncheck
        cand.push_back(pii(y, x));
      }

    } else {

      continue;
    }
  }
  return false;
}

int main() {
  In();
  FindAns();
  Print();

  return 0;
}