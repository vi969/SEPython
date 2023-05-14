import sys

chapter = sys.argv[1]
page = sys.argv[2]
dots_quantity = 38 - len(chapter) - len(page)
print(chapter, "." * dots_quantity, page)

