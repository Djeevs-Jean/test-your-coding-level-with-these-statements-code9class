import re

def re_ip_adress(expression=None):
    expression = r"([0-9]{3})([.]{1}[0-9]{,3}){3}"
    password = input("Entrer un address IP: ")
    compile = re.compile(expression).match(password)
    if compile is not None: return password
    else:
        print("Entrer une addresse IP valide.")
        return re_ip_adress(expression)

def operation_ip(value):
    operation = [int(i) for i in str(value) if i.isdigit()]
    return sum(operation) * operation[0]

print(
    operation_ip(re_ip_adress())
)