s = input("Enter the main string: ")
sub = input("Enter the substring: ")

count = 0
for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        count += 1

print("Substring occurs:", count, "times")




# Enter the main string: abcabci
# Enter the substring: abc
# Substring occurs: 2 times
