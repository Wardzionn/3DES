from bitarray import bitarray
import convert
import bitops
import permutation
import tables
import algorithm
#
# # a = bitarray(64)
# # a.setall(0)
# # a[4]=1
# #
# # print(a)
# #
# # string = "dupa"
# #
# # binary = convert.ascii_to_bin(string)
# # print(binary)
# #
# #
# # x =10
# # y = 3
# #
# # print(x//y)
# # print(x%y)
# a = "dupaupaa"
# key = list()
#
#
# encoded = bitarray("00100110100011011100010000111000101100011101110001101100101001111110100111101000101011101000011101000110010001110100011111101110")
#
# #key.append("4OC9OGM6")
# key.append("vlEsz9CU")
# key.append("4OC9OGM6")
# #key.append("vlEsz9CU")
# #key.append("4OC9OGM6")
# #key.append("vlEsz9CU")
#
#
# key.append("TzoHyq7e")
#
# #manual 3des encryption
# b = algorithm.des(a, key[0], "e")
# print(b)
# b = algorithm.des(b, key[1], "d")
# print(b)
# b = algorithm.des(b, key[2], "e")
#
# print(b)
#
# b = algorithm.des(b, key[2], "d")
# print(b)
# b = algorithm.des(b, key[1], "e")
# print(b)
# b = algorithm.des(b, key[0], "d")
# print(b)
#
#
#
# #sztring = "00111000111110100111101101101001010011101100010011111001100111110001110001100100100111001011101101010000000010101011000101000001"
# # z = algorithm.triple_des_encryption(a, key[0], key[1], key[2])
# #
# # #c = algorithm.triple_des_decryption(b, key[0], key[1], key[2])
# #
# # print(z)
# # #print(c)
#
#
#
#
#
#
a = bitarray('001011001011001011001011001011001011001011001011')
b = bitops.shift(a, 2)
print(b)