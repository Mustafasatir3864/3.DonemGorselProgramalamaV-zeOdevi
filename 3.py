ifade = input('ifadeyi girin: ')
aranan = input('aranan ifadeyi girin: ')

x = ifade.index(aranan)

print(ifade[x-1] + aranan + ifade[x+len(aranan)+1])
