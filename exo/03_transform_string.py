def transform_string(value):
    word = str(value).split()
    word = [i.lower() for i in word]
    word = [text[0].upper()+text[1:] for text in word]
    print(word)

transform_string("Ayiti se yon BEL PEYI")