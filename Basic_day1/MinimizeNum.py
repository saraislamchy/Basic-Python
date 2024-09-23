def maximum(N, A):
    count = 0

    while True:

        even = True
        for num in A:
            if num % 2 != 0:
                even = False
                break

        if not even:
            break
        A = [num // 2 for num in A]
        count += 1

    return count

N = int(input())
A = list(map(int, input().split()))

print(maximum(N, A))
