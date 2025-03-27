from collections import Counter

def most_frequent_words(filename):
    with open(filename, 'r') as file:
        words = file.read().lower().split()

    word_count = Counter(words)
    most_common = word_count.most_common(10)

    print("Top 10 most frequently occurring words:")
    for word, count in most_common:
        print(f"{word}: {count}")

# Call function with a file path, e.g., "sample.txt"
most_frequent_words("sample.txt")
