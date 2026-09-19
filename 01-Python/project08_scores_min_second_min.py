
#scores = [19, 20, 18, 17]

scores = [21, 3, 13, 5, 18, 2, 22,1]

if scores[0] < scores[1]:
    minimum = scores[0]
    second = scores[1]
else:
    minimum = scores[1]
    second = scores[0]

for score in scores[2:]:
    if score < minimum:
        second = minimum
        minimum = score
    else:
        if score < second:
            second = score

print("minimum:",minimum)
print("second:", second)