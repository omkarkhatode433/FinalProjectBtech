import binascii
key="hii  "
keydemo=key.encode()
str = binascii.hexlify(keydemo).decode('utf-8')
keydemo = str[0:32]
print(keydemo)