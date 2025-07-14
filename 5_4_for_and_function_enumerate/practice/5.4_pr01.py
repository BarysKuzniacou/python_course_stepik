words = input()

lst = []

for i in range (len(words)-1):
    if words.find('ра') == -1:
        lst.append(-1)
        break
    if words[i] == 'р' and words[i+1] == 'а':
        lst.append(i)
        i += 1

print(*lst)