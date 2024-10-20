"""
CP1404/CP5632 Practical
Estimated completion time 10 minutes
"""

text = input("Text: ")

word_to_count = {}

for word in text.split():
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

sorted_words_counts = sorted(word_to_count.items())

# Find length of longest word for formatting
max_length = max(len(word) for word, count in sorted_words_counts)

for word, count in sorted_words_counts:
    print(f"{word:{max_length}} : {count}")
