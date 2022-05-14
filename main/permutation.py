import tables
import convert
import bitops
from bitarray import bitarray


# simple permutation using a specified table
def basic(permutation_table, to_permutate):

    permutated = bitarray()
    for i in permutation_table:
        permutated.append(to_permutate[int(i) - 1])
    return permutated


# permutation using s-boxes
def get_box_coordinates(_6bits):
    row = convert.bin_to_dec(str(_6bits[0]) + str(_6bits[-1]))
    column = convert.bin_to_dec(str(_6bits[1])+str(_6bits[2])+str(_6bits[3])+str(_6bits[4]))
    return row, column


def sbox(input48):
    current6bits = bitarray()
    result32 = bitarray()
    chunks = bitops.split_bitarray_into_chunks(input48, 6)
    for i in range(8):
        #current6bits.append(bitops.split_into_chunks(input48, 6)[i])
        row, column = get_box_coordinates(chunks[i])
        result32.extend(convert.dec_to_bin(tables.SBOX[i][row][column]))
        #current6bits.clear()
    return result32
