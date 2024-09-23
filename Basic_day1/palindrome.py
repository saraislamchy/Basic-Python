n = input()
reverse = n[::-1]
x = reverse.lstrip('0')
print(x)
 
if n==reverse:
    print("YES")
else:
    print("NO")