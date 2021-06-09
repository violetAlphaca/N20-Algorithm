#include <iostream>
#include <algorithm>

using namespace std;

int R, C;
char Map[20][20];
bool visit[26] = {false};
int maxx = 0;

int dy[] = {0, 0, 1, -1};
int dx[] = {1, -1, 0, 0};

void In() {
  char tmp;
  cin >> R >> C;
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      cin >> tmp;
      Map[i][j] = tmp;
    }
  }
}

bool IsInside(int y, int x) {
  return y >= 0 && y < R && x >= 0 && x < C;
}

void FindAns(int y, int x, int counter) {
  if (visit[Map[y][x] - 'A']) {
    maxx = max(maxx, counter);
    return;
  }

  visit[Map[y][x] - 'A'] = true;
  for (int d = 0; d < 4; d++) {
    int next_y = y + dy[d];
    int next_x = x + dx[d];
    if (IsInside(next_y, next_x)) {
      FindAns(next_y, next_x, counter + 1);
    }
  }
  visit[Map[y][x] - 'A'] = false;
}

int main() {
  In();
  FindAns(0, 0, 0);
  cout << maxx << endl;

  return 0;
}