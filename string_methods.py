# txt.zfill(number_of_values)
a = '10'  # 00010
b = 'hello'  # hello
c = ''  # 00000
d = 'd'  # 0000d
print(c.zfill(5))  # Fills the string with a specified number of 0 values at the beginning

# обрізає рядок по вказаним елементам в параметрах
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)  # banana

# .rsplit та .lsplit аналогічні методи, але має параметр maxsplit
# string.rsplit(separator, maxsplit)
#
# Parameter 	Description
# separator 	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
# maxsplit 	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"