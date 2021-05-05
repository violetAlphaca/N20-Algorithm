n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
originalProduct = 0

for i in range(n):
    originalProduct += A[i]*B[i]
ans = originalProduct

for pivot in range(1, n):
    # pivot is the element
    current = originalProduct
    for wing in range(1, n):
        if pivot - wing < 0 or pivot + wing >= n:
            break
        current -= A[pivot-wing]*B[pivot-wing]+A[pivot+wing]*B[pivot+wing]
        current += A[pivot-wing]*B[pivot+wing]+A[pivot+wing]*B[pivot-wing]
        ans = max(current, ans)

    # pivot is between the elements
    current = originalProduct
    for wing in range(1, n):
        if pivot - wing < 0 or pivot + wing - 1 >= n:
            break
        current -= A[pivot-wing]*B[pivot-wing]+A[pivot+wing-1]*B[pivot+wing-1]
        current += A[pivot-wing]*B[pivot+wing-1]+A[pivot+wing-1]*B[pivot-wing]
        ans = max(current, ans)

print(ans)
