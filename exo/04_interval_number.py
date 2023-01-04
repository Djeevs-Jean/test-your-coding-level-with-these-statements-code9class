import random

INTERVAL_NUMBER = list(range(1, 21))

def multipleA_and_Not_multipleB(valA, valB):
    return [i for i in INTERVAL_NUMBER if i % valA == 0 and i % valB !=0]

def multipleB_and_Not_multipleA(valA, valB):
    return [i for i in INTERVAL_NUMBER if i % valB == 0 and i % valA !=0]
    
def multipleA_and_multipleB(valA, valB):
    return [i for i in INTERVAL_NUMBER if i % valA == 0 and i % valB == 0]

def not_multipleA_and_multipleB(valA, valB):
    return [i for i in INTERVAL_NUMBER if i % valA != 0 and i % valB != 0]

# test

n1 = multipleA_and_Not_multipleB(2,3)
print(f"{n1} -> total number: {len(n1)}")

n2 = multipleB_and_Not_multipleA(2,3)
print(f"{n2} -> total number: {len(n2)}")

n3 = multipleA_and_multipleB(2,3)
print(f"{n3} -> total number: {len(n3)}")

n4 = not_multipleA_and_multipleB(2,3)
print(f"{n4} -> total number: {len(n4)}")
