import  sys

string = sys.argv[1]
string_replace = string.strip().replace("<br>", "\n")
print(string_replace)
