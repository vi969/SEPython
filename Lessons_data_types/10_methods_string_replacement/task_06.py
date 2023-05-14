import sys
word = sys.argv[1]
word = word.replace("</b><b>", "")
print(word)