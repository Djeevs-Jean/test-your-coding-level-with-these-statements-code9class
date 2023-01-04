from math import prod

def product_number(value):
    value = str(value).split()
    sum_value = [sum([int(jK) for jK in iV]) for iV in value]
    return prod(sum_value)

print(product_number("5 45 123 12"))