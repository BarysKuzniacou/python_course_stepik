# put your python code here
word_first, word_second = map(str, input().split())
print(word_first in word_second, word_first == word_second, word_first > word_second, word_first < word_second)