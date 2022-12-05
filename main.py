import sys
import time
import array

start_time = time.time()

# test_number = "abcde"
# str_ascii = [ord(i) for i in test_number]
# str_map_filter = list(filter(lambda i: i > 98, map(ord, test_number)))
# str_map_filter = tuple(ord(i) for i in test_number)
# str_array = array.array("i", (ord(i) for i in test_number))


# # str_map_filter = list(filter(lambda i: i > 98, map(ord, test_number)))
# # print(str_map_filter)

colors = ["black", "white"]
sizes = ["S", "M", "L"]
t = [(color, size) for color in colors for size in sizes]
print(t)
print(sys.getsizeof(t))
# # a = []
# # for color in colors:
# #     for size in sizes:
# #         a.append((color, size))
# # print(a)

# end = time.time() - start_time
# print(end*1000000)

for t in ("%s %s" % (c, s ) for c in colors for s in sizes):
    sys.getsizeof(t)
"""
black S
black M
black L
white S
white M
white L
"""