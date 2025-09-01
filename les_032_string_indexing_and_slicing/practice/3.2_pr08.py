word_first, word_second = map(str, input().split())
length_word_second = len(word_second)
word_first = word_first[1:length_word_second:2]
word_second = word_second[1::2]
print(word_first == word_second)