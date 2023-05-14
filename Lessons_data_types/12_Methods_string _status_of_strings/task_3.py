import sys
incoming_file = sys.argv[1]
is_png_file = incoming_file.lower().endswith(".png")
print(is_png_file)