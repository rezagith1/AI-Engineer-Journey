

def calculate_tax(price, tax=10):

    tax_met = price * tax/100
    final = price + tax_met
    return final

result = calculate_tax(100000)
print(result)

result = calculate_tax(100000 , 20)
print(result)


def test():
    x = 20
    
    print(x)






