import random

import string


def generate_password(length=8, chars=False, digits=False):

    characters = string.ascii_letters

    if chars:
        characters += string.punctuation 

    if digits:
        characters += string.digits

    if length < 1:
        length = 8

    password = ''.join(random.choice(characters) for _ in range(length))


generate_password(length=10, chars=True, digits=True)


