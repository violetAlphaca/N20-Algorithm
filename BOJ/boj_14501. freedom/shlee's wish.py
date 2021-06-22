data = [0 for _ in range(int(input()))]
for i in range(len(data)):
    day, value = map(int,input().split(" "))
    if i > 0:
        value = value + data[i-1]
    if i+day-1 < len(data) and value > data[i+day-1]:
        for j in range(i+day-1, len(data)):
            if data[j] > value:
                break
            data[j] = value
print(data[-1])