import bitops
from bitarray import bitarray


# to binary
def ascii_to_bin(text):
    # binary = bitarray()
    # # binary.frombytes(text.encode('utf-8'))
    # dec = []
    # binary_list = bitarray()
    # for i in text:
    #     dec.append(ord(i))
    # for i in dec:
    #     binary.append(int(bin(i)[2:]))
    #     while len(binary) < 8:
    #         binary = '0' + binary
    #     binary_list.append(binary.to01())
    #     binary.clear()
    # return binary_list
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
