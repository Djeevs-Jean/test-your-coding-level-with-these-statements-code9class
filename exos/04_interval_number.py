import random

INTERVAL_NUMBER = list(range(1, 21))

def multipleA_and_Not_multipleB(valA, valB):
    return [i for i in INTERVAL_NUMBER if i % valA == 0 and i % valB !=0]

def multipleB_and_Not_multipleA(valA, valB):
    return [i for i in INTERVAL_NUMBER if i % valB == 0 and i % valA !=0]
    

print(
    multipleA_and_Not_multipleB(2,3),
    multipleB_and_Not_multipleA(2,3)
)
# def multiple()