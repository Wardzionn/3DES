import bitops
from bitarray import bitarray


# to binary
def ascii_to_bin(text):
    result = bitarray()
    for c in text:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        while len(bits) < 8:
            bits = '0' + bits
        result.extend([int(b) for b in bits])
    return result


def dec_to_bin(dec):
    dec = bin(dec)[2:].zfill(4)
    binn = bitarray(str(dec))
    return binn


# from binary
def bin_to_dec(binary):
    dec = int(str(binary), 2)
    return dec


def bin_to_ascii(binary):
    chars = bitops.split_bitarray_into_chunks(binary, 8)
    result = ""
    for i in range(len(chars)):
        char = chars[i].to01()
        result += chr(int(char, 2))
    return result


# hex
def hex_to_bin(key):
    dictionary = {
        '0': "0000",
        '1': "0001",
        '2': "0010",
        '3': "0011",
        '4': "0100",
        '5': "0101",
        '6': "0110",
        '7': "0111",
        '8': "1000",
        '9': "1001",
        'A': "1010",
        'B': "1011",
        'C': "1100",
        'D': "1101",
        'E': "1110",
        'F': "1111"}
    bin_key = bitarray()
    for i in range(len(key)):
        temp = bitarray(dictionary[key[i]])
        bin_key.extend(temp)
    return bin_key
