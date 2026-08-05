
name = input("what is your name? ")
age = int(input("How old are you? "))
Status = input("Are you a student? ")
      
if age <= 0 or age > 120:
    print("Invalid age")
else:
    print("hello" ,name )    
    if  0 < age < 13: 
    
        print("you are a child.")
    elif 13 <= age <= 17:  
        print("you are a teenager.")
    elif 18 <= age <= 64:
        print("you are an adult.")    
    elif age >= 65: 
        print("you are an senior.")        

    if 18 <= age <= 64:
       if Status=="yes":
          print("Adult Student") 
       else:
          print("Adult Non-Student")       