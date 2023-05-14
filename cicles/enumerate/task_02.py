import sys
files_count = int(sys.argv[1])
text = sys.argv[2]

start = 0
for f in range(1, files_count + 1):
    file = open(f"data-{f}.txt", "w+", encoding="utf-8")
    for i in range(start, len(text), files_count):
        if len(text) - 1 >= i:
            file.write(text[i])
        else:
            break
    start += 1

