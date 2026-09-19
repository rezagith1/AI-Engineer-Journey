
above_average_count=0
count = 0
total = 0
Average = 0
scores = [12, 8, 17, 5, 19, 7, 15, 20]

for score in scores:
      #count +=1 
      total += score
      count +=1 
Average = total /count

for score in scores:
       if score > Average:
              above_average_count += 1
              print(score)
print("above_average_count:" , above_average_count )
print("avarag:" ,Average)
       