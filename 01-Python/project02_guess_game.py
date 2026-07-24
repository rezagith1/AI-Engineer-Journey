
print("Welcome to Guess Game")
secret=int(input("Guess the number:"))

while secret != 7:
    
    if secret < 7:
       print("Too Low") 
    else:
       print("Too High")

    secret=int(input("Guess the number:"))     
    print("Congratulations!")



