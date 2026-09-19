
count = 0
total = 0
Average = 0
scores = [12, 8, 17, 5, 19, 7, 15, 20]

for score in scores:

   if score < 10:
       continue

   print(score)
     
   count +=1 
   total += score
    
Average = total /count
print("count:" , count )
print("avarag:" ,Average)
       
       