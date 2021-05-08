from functools import reduce

N, K = map(int, input().split())

# Out of Bound Cases
# 1. 두 자릿수 인데 일의 자리가 0
# 2. 한 자릿수인 경우

_strN = str(N)
M = len(_strN)


def _swap(s, i, j):
    if i == 0 and s[j] == 0:
        return -1
    else:
        return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]


def bfs(strN):
    answer = 0
    q = []
    visited = [{}]
    q.append([strN, 0])

    while len(q) > 0 and q[0][1] < K:
        cur, depth = q.pop(0)
        depth += 1
        if len(visited) == depth:
            visited.append({})

        for i in range(M):
            for j in range(i + 1, M):
                newStr = _swap(cur, i, j)
                if visited[depth].get(newStr) != True:
                    visited[depth][newStr] = True
                    q.append([newStr, depth])

    intedQ = list(map(lambda x: int(x[0]), q))
    intedQ.sort()
    return intedQ[-1]


if M == 1 or (M == 2 and N % 10 == 0):
    print(-1)
else:
    print(bfs(_strN))
