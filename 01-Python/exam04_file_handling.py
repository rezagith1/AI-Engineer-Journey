
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("سلام رضا\n")
    file.write("در حال یادگیری Python هستم.\n")
    file.write("هدف من AI Engineer شدن است.\n")

with open("notes.txt", "r", encoding="utf-8") as file:
       content = file.read()

print(content)