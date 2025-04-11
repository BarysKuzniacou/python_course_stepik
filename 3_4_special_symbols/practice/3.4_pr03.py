text = input()
text = text.replace(" ", "\"")
text = text.replace("\"", "\'", 1)
print(text)