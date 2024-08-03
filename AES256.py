from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

secretkey = os.urandom(32) #32*8 = 256
cipher = AES.new(secretkey, AES.MODE_CBC)

data = 'Тест!'.encode('utf-8')
result = cipher.encrypt(pad(data, AES.block_size))

print(f'Зашифровано! {result}')