tittle=int(input("Enter a number greater than or greater than 0 or less than 8640000: "))


days = 86400
hours = 3600
minutes = 60

days,remainder1 = divmod(tittle,days)

hours,remainder2 = divmod(remainder1,hours)

minutes,seconds = divmod(remainder2,minutes)

last_two = days % 100
last_one = days % 10

if 11 <= last_two <= 14:
    word = "днів"
elif last_one == 1:
    word = "день"
elif last_one in [2, 3, 4]:
    word = "дні"
else:
    word = "днів"

print(f"{days}{word},{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")






























