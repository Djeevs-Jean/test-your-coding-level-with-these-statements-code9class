import string

ALPHA = string.ascii_letters[:26] 

def separated_character(value)->dict:
    dict_data = dict()
    dict_data["sign"] = ''.join([i for i in str(value) if i in ['>', '<']])
    dict_data["number"] = int(''.join([ i for i in str(value) if i.isdigit()]))
    dict_data["word"] = ''.join([ i for i in str(value) if i.isalpha()])
    return dict_data

def render(value)->str:
    dict_data = separated_character(value)

    if dict_data["number"] == 0: return dict_data["word"]
    index = ALPHA.index(dict_data["word"])

    if dict_data["sign"] == '>':
        return ALPHA[index+dict_data["number"]]
    else: 
        return ALPHA[index-dict_data["number"]]

def run(value):
    value = str(value).lower().split()
    text = str()
    for i in value: text += render(i)
    print(text)

run("<1T >7H >3C <5Y >13J <2C <5W >4A")
run(">3A >0A <1U <10K >1A <9J <0S <16U")