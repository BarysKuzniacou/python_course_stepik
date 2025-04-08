# put your python code here
word_first, word_second = map(str, input().split())
length_word_first = len(word_first)
print(word_second[:length_word_first])