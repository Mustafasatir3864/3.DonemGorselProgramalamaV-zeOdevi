import re

ifade = input('ifadeyi girin :')

if re.match(r"[^@]+@[^@]+\.[^@]+", ifade):
    print("email adresidir.")
else:
    print("email adresi değidir.")