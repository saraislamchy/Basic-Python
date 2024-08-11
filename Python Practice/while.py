#1 while loop
num = 1
while num <= 5:  
    print(num)
    num +=1


#2 while with if elif :
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num, "is even")   
    else:
        print(num, "is odd")

    num += 1  


#3 while with continue
num = 1
while num <= 5:
    if num % 2 == 0:
        num += 1
        continue
    print(num)
    num += 1



#4 while with break
num = 1
while True:
    print(num)
    if num > 5:
        break
    num += 1