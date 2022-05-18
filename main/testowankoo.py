from bitarray import bitarray
import convert
import bitops
import permutation
import tables
import algorithm
from Crypto.Cipher import DES3
from Crypto import Random

key = '123456789'
iv = Random.new().read(DES3.block_size) #DES3.block_size==8
cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)
plaintext = 'sona si latine loqueri  ' #padded with spaces so than len(plaintext) is multiple of 8
encrypted_text = cipher_encrypt.encrypt(plaintext)
