import re

ifade = input('ifadeyi girin :')

regex = "(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)"

if re.match(regex, ifade):
    print("Geçerli bir url adresidir.")
else:
    print("Geçerli bir url değidir.")