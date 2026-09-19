
#def add(a,b):
#    print(a+b)


#add(10,30)   
def factorial():

    fact = 1
    number = int(input("Please enter a number: "))

    for i in range(1, number + 1):
        fact = fact * i

    print("Factorial is:", fact)

factorial()


