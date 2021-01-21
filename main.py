import string
import random


def generator(size=5, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


print(generator(int(input('How many characters in your password : '))))

