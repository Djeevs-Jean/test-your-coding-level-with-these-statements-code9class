def asterisk_vowels(value):
    value = str(value).split()
    value = '^'.join(value)
    vowels = ["a", "e", "i", "o", "u", "y"]
    value = ''.join(["*" if i.lower() in vowels else i for i in value]).replace("^", " ")
    print(value)

asterisk_vowels("T H A M A R - Pou Toutan")