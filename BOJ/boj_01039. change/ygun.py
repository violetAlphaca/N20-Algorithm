from functools import reduce

N, K = map(int, input().split())

_strN = str(N)
M = len(_strN)

def _swap(s, i, j):
    if i == 0 and s[j] == 0:
        return -1
    else:
        return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

# Early Termination: 이미 가능한 최댓값이 됐으면, 그 후 짝수 연산은 무시하고 최댓값 리턴
# 홀수 연산은 마지막과 마지막-1 자리만 바꿔주면 됨.
# 단, 동일한 수가 하나라도 존재하는 경우(anyDuplicates) 무조건 최댓값 리턴
def bfs(strN):
    answer = 0
    q = []
    visited = [{}]
    q.append([strN, 0])
    maximumList = [x for x in strN]
    maximumList.sort(reverse=True)
    maximumValue = reduce(lambda acc, cur: acc + cur, maximumList, '')
    anyDuplicates = len(dict.fromkeys(maximumValue, True)) < M

    while len(q) > 0 and q[0][1] < K:
        cur, depth = q.pop(0)
        depth += 1
        if len(visited) == depth:
            visited[-1] = {}
            visited.append({})

        for i in range(M):
            for j in range(i + 1, M):
                newStr = _swap(cur, i, j)
                if visited[depth].get(newStr) != True:
                    visited[depth][newStr] = True
                    q.append([newStr, depth])

                    # Early Termination
                    if maximumValue == newStr:
                        if (K - depth) % 2 == 0 or anyDuplicates:
                            return maximumValue
                        else:
                            return _swap(maximumValue, M-2, M-1)

    intedQ = list(map(lambda x: int(x[0]), q))
    intedQ.sort()
    return intedQ[-1]

# Out of Bound Cases
# 1. 두 자릿수 인데 일의 자리가 0
# 2. 한 자릿수인 경우
if M == 1 or (M == 2 and N % 10 == 0):
    print(-1)
else:
    print(bfs(_strN))
