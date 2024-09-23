"""def balanceString(S):
    left_count = 0
    right_count = 0
    result = []
    balanceString = ""

    for char in S:
       balanceString += char
        if char == 'L':
            left_count += 1
        elif char == 'R':
            right_count += 1
        
        if left_count == right_count:
            result.append(balanceString)
            balanceString = ""
            left_count = 0
            right_count = 0
    
    print(len(result))
    for substring in result:
        print(substring)

# Read input
S = input().strip()

# Split the balanced string and print the results
balanceString(S) 
"""

"""def balanceString(S):
    left_count = 0
    right_count = 0
    result = []
    balanceString = ""

    for char in S:
       balanceString += char
        if char == 'L':
            left_count += 1
        elif char == 'R':
            right_count += 1
        
        if left_count == right_count:
            result.append(balanceString)
            balanceString = ""
            left_count = 0
            right_count = 0
    
    print(len(result))
    for substring in result:
        print(substring)

# Read input
S = input().strip()

# Split the balanced string and print the results
balanceString(S) 
"""

def balancedString(S):
    left = 0
    right= 0
    result = []
    balancedString = ""

    for char in S:
        balancedString += char
        if char == 'L':
            left += 1
        elif char == 'R':
            right += 1
        
        if left == right:
            result.append(balancedString)
            balancedString = ""
            left = 0
            right = 0
    
    print(len(result))
    for substring in result:
        print(substring)


S = input().strip()


balancedString(S)
