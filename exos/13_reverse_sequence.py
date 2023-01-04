# # def reverse_sequence():
# #     values = [0, 1, 2, 3, 4]

# #     for i in len(values)-1:
# #         val = values
# #         seq = val
# #         reverse_ = val.reverse()
# #         print(f"{seq} -> {reverse_}")

# # reverse_sequence()

# values = [0, 1, 2, 3, 4]
# print(values)
# values = reversed(values).
# print(values)


def reverse_number():

    L = [0,1,2,3,4]
    for i in range(len(L)-1):
        print("{}-> {}".format(L, L[::-i]))
        L = L[::-1]

reverse_number()
