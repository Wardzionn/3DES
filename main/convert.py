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


def hex_to_bin(array):
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
        'a': "1010",
        'b': "1011",
        'c': "1100",
        'd': "1101",
        'e': "1110",
        'f': "1111"}
    bin_output = bitarray()
    for i in range(len(array)):
        temp = bitarray(dictionary[array[i]])
        bin_output.extend(temp)
    return bin_output


def bin_to_hex(array):
    dictionary = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'a',
          "1011": 'b',
          "1100": 'c',
          "1101": 'd',
          "1110": 'e',
          "1111": 'f'}
    hex_output = ""
    for i in range(0, len(array), 4):
        temp = ""
        temp = temp + array[i]
        temp = temp + array[i + 1]
        temp = temp + array[i + 2]
        temp = temp + array[i + 3]
        hex_output = hex_output + dictionary[temp]

    return hex_output