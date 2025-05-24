# using Dictionary

text = input("Enter a sentence: ")

words = text.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Find the word with the highest frequency
max_word = ""
max_count = 0

for word in freq:
    if freq[word] > max_count:
        max_count = freq[word]
        max_word = word

print("Most frequent word:", max_word)
print("Frequency:", max_count)
