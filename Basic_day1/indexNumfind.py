arr = input("Enter elements separated by space: ").split()
target = input("Enter element to find: ")

index = -1
for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break

if index != -1:
    print(f"Element found at index: {index}")
else:
    print("Element not found")
