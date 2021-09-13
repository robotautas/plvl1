from random import randint


def random_password(length):
    password = ''
    for i in range(1, length+1):
        symbol = chr(randint(33, 126))
        password += symbol
    return password

for i in range(10):
    print(random_password(20))