# Question: Implement a Python function to convert a string containing binary digits into its equivalent decimal representation.
#
# Example binary string:
# binary_str = "110101"

def convert_str_binary_to_int(binary_str):
    return sum([int(i)*count for count, i in enumerate(binary_str[::-1], start=1)])

print(convert_str_binary_to_int("110101"))
print(convert_str_binary_to_int("110"))
print(convert_str_binary_to_int("101"))
