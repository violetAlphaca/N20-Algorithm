# back tracking
N = int(input())
# index starts from 1
time = [0]
price = [0]
ans = 0
for day in range(1, N + 1):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)


def back(day, selected):
    if day == N + 1:
        # sum up and update the ans
        global ans
        localAns = 0
        for i in selected:
            localAns += price[i]
        ans = max(localAns, ans)
    else:
        # make new combination and back track
        for nextDay in range(day, N + 1):
            # End condition: the last day
            if day + time[nextDay] > N + 1:
                back(N + 1, selected)
            else:
                back(nextDay + time[nextDay], selected + [nextDay])


back(1, [])

print(ans)
