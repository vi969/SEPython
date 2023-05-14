import sys
incoming_file = sys.argv[1]
incoming_file = incoming_file.lower()
is_png_file = incoming_file.endswith(".png")
is_jpg_file = incoming_file.endswith(".jpeg") or incoming_file.endswith(".jpg")
is_gif_file = incoming_file.endswith(".gif")

is_image = is_png_file or is_jpg_file or is_gif_file
print(is_image)
