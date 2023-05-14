import sys

str_format = sys.argv[1]
dashes = "+{dash:^29}+".format(dash="-" * 29)
text = "| {:^27} |".format(str_format)
print(dashes, text, dashes, sep="\n")
