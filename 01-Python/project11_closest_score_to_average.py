
count = 0
total = 0
Average = 0
#scores = [12, 8, 17,13, 19, 7, 15, 20]

scores = [2, 4, 6, 20, 22, 24]
for score in scores:
      #count +=1 
      total += score
      count +=1 
average = total /count

difference = abs(scores[0] - average)

closest_difference = difference
closest_score = scores[0]

for score in scores[1:]:
      difference = abs(score - average)
      if difference <= closest_difference:
         closest_difference = difference
         closest_score = score
print("closest_difference =" , closest_difference  )
print("avarag:" ,average)
print("closest_score =" ,closest_score )       