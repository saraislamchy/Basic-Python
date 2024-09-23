"""def goodSeq(N, a):
    from collections import Counter

    frequency = Counter(a)
    r = 0


    for x, count in frequency.items():
        if count < x:
            r += count
        else:
            r += count - x

    return r

N = int(input())
a = list(map(int, input().split()))

print(goodSeq(N, a))
"""

def goodSeq(N, a):
    from collections import Counter

    freq = Counter(a)
    removals = 0


    for x in freq:
        count = freq[x]
        if count < x:
            removals += count
        else:
            removals += count - x

    return removals


N = int(input())
a = list(map(int, input().split()))
print(goodSeq(N, a))
