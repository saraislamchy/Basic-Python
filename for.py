for i in range (5):
    print(i)
# Output: 0, 1, 2, 3, 4


for i in range (2,5):
    print(i)
# Output: 2, 3, 4

for i in range ( 1, 10, 2):   #start, stop, step argument
    print(i)

# for loop with if-elif
for num in range (1, 11):
    if num % 2 ==0:
        print(num, "is even")
    else:
        print(num, "is odd")   


# for loop with String
w = "python"

for char in w:
    print(char)


# for loop with list
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)