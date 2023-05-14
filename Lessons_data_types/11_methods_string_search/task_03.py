import sys

tags = sys.argv[1]
value_of_header = sys.argv[2]

header_start_index = tags.find("<h1>") + 4
header_end_index = tags.find("</h1>")

start_string = tags[:header_start_index]
end_string = tags[header_end_index:]
print(start_string,value_of_header,end_string, sep="")