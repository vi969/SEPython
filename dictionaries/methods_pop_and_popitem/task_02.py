import sys
key_name = sys.argv[1]

game = {
   "name": "Cyberpunk 2077",
   "price": 3900,
   "genre": "action"
}

# upper_item = key_name.upper()
# item_value = game[key_name]
# game.pop(key_name)
# game[upper_item] = item_value
# print(game)

get_value = game.pop(key_name)
game[key_name.upper()] = get_value
print(game)