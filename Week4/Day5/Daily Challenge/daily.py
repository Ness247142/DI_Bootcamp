# Write a Python function to reverse the bits of an integer (32 bits unsigned).
# Input : 1234
# Output : 1260388352
# For example, 1234 represented in binary as 10011010010 and returns 1260388352 which represents in binary as 01001011001000000000000000000000

# FUNCTION to reverse the bits of an integer
def reverse_bits(x):
    bits = 0
    for i in range(0, 32):
        bits <<= 1
        bits = bits | x & 1
        x >>= 1
    return bits


print(reverse_bits(1234))
