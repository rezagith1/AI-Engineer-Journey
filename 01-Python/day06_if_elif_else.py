name = input("what is your name? ")
age = int(input("How old are you? "))

print("hello", name)

if age < 0 or age > 120:
    print("invalid age")
elif age >= 120:
    print("invalid age")    
elif age < 13:
    print("you are a child.")
elif age < 18:
    print("you are a teenager.")    
elif age < 65:
    print("you are an adult.")    
else:
    print("you are a senior.")    