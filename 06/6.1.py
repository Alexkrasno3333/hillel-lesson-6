import string

first_letter = input("Enter your letters: ")

title = string.ascii_letters

start, end = first_letter.split("-")

cut1 = title.index(start)
cut2 = title.index(end)
cutsum = title[cut1:cut2+1]
print(cutsum)













































