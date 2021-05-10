#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens,
                                        vector<int>& king) {
  vector<vector<int>> answers;
  vector<bool> visit_tmp(8, false);
  vector<vector<bool>> q_map(8, visit_tmp);

  // locate queens
  for (auto q : queens) {
    q_map[q.front()][q.back()] = true;
  }

  for (auto q : queens) {
    if (IsUnderAttack(q, king, q_map)) {
      answers.push_back(q);
    }
  }
  return answers;
}

bool IsUnderAttack(vector<int>& q, vector<int>& king,
                   vector<vector<bool>>& q_map) {
  int q_y = q.front();
  int q_x = q.back();
  int k_y = king.front();
  int k_x = king.back();
  if (q_y == k_y || q_x == k_x || abs(q_y - k_y) == abs(q_x - k_x)) {
    int y_inc = (k_y - q_y) > 0 ? 1 : (k_y - q_y) < 0 ? -1 : 0;
    int x_inc = (k_x - q_x) > 0 ? 1 : (k_x - q_x) < 0 ? -1 : 0;
    while (q_y != k_y || q_x != k_x) {
      q_y += y_inc;
      q_x += x_inc;
      if (q_map[q_y][q_x]) {
        return false;
      }
    }
    return true;
  }
  return false;
}

int main() { return 0; }
