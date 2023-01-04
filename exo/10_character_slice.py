def character_slice(value):
    value_index = str(value).index(";")
    return value[value_index+1:]


print(character_slice("web-insecure;34829sjdfnsj32984madsdkj"))