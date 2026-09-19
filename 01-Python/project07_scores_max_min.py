scores = [19, 20, 18, 17]

if scores[0] > scores[1]:
    maximum = scores[0]
    second = scores[1]
else:
    maximum = scores[1]
    second = scores[0]

for score in scores[2:]:
    if score > maximum:
        second = maximum
        maximum = score
    else:
        if score > second:
            second = score

print("maximum:", maximum)
print("second:", second)
