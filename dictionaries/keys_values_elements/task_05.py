import sys


nick_name = sys.argv[1].lower()

users = {
   "user1@domain.com": "nikitos",
   "user2@domain.com": "black adam",
   "user3@domain.com": "minion",
   "user4@domain.com": "lovey",
   "user5@domain.com": "barbie",
   "user6@domain.com": "comedy central",
   "user7@domain.com": "bro",
   "user8@domain.com": "rapunzel"
}

users_values = list(users.values())
is_nick = nick_name in users_values
print(is_nick)

