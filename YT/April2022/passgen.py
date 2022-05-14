import random

from certifi import where
passlen = int(input("Enter the length of Password: "))
small ="abcdefghijklmnopqrstuvwxyz"
cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sym ="!@#$%^&*()?"
num ="01234567890"


if passlen >= 6 and passlen <= 13:
    p = "".join(random.sample((small+cap+sym+num),passlen))
    print(f'Your password is {p}')
elif passlen <= 6:
    print("Password length should be greater than 6")
else:
    print("Password length should be less than 13")

