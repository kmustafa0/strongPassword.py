import string
import random

characters = list(string.ascii_letters + string.digits + "-_\/!@#$½^&*()")

def random_password():
    length = int(input("Şifre uzunluğunu gir: "))

    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))


    random.shuffle(password)

    print("".join(password))

random_password()