import sys

tags = sys.argv[1]

header_start = tags.find("<h1>") + 4
header_end = tags.find("</h1>")

print(tags[header_start:header_end])