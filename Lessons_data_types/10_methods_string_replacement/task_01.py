import sys

pronoun_be = sys.argv[1]

pronoun_be = pronoun_be.\
    replace("I am", "I'm").\
    replace("You are", "You're").\
    replace("He is", "He's").\
    replace("She is", "She's").\
    replace("It is", "It's").\
    replace("We are", "We're").\
    replace("They are", "They're")

print(pronoun_be)