letter = input("Enter your Letter: ")
freq = {}

for l in letter:
    l = l.lower()
    if 'a' <= l <= 'z':
        if l in freq:
            freq[l] += 1
        else:
            freq[l] = 1

for key in freq:
    print(key, ":", freq[key])