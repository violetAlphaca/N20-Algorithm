#include <algorithm>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

int N, K;

void In() { cin >> N >> K; }

int maxx = -1;

void FindAns() {
  string cur;
  vector<string> q;
  vector<string> buffer;
  set<string> visit;
  q.push_back(to_string(N));
  int counter = 0;

  while (counter < K) {
    counter++;

    while (!q.empty()) {
      cur = q.back();
      q.pop_back();

      for (int i = 0; i < cur.size(); i++) {
        for (int j = i + 1; j < cur.size(); j++) {
          if (i == 0 && cur[j] == '0') continue;
          swap(cur[i], cur[j]);
          if (visit.find(cur) == visit.end()) {
            visit.insert(cur);
            buffer.push_back(cur);
          }
          swap(cur[i], cur[j]);
        }
      }
    }
    visit.clear();
    while (!buffer.empty()) {
      q.push_back(buffer.back());
      buffer.pop_back();
    }
  }

  while (!q.empty()) {
    cur = q.back();
    q.pop_back();
    maxx = max(maxx, stoi(cur));
  }
}

int main() {
  In();
  FindAns();

  cout << maxx << endl;

  return 0;
}
