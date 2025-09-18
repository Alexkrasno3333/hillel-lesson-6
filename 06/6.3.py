tittle = input("Enter your number: ")
if len(tittle)==1:
    print(tittle)
else:

    while len(tittle) > 1:
        product = 1
        for i in tittle:
            i = int(i)
            product *= i
        tittle = str(product)
    print(product)
















