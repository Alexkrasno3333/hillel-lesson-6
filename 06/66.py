def coffee_decorator(func):
    def wrapper(*args, **kwargs):
        double = kwargs.get('double', False)
        milk = kwargs.get('milk', 0)
        suger = kwargs.get('suger', 0)
        dis = []
        if milk > 0:
            if milk == 1:
               dis.append(" з молоком ")
            if milk == 2:
                dis.append("з подвійним молоком")

        if suger > 0:
            if suger == 1:
                dis.append("з цукром")
            if suger== 2:
                dis.append("з подвійним цукром")

        final_text = " та ".join(dis)
        if double:
            final_text += " подвійна кава"
        elif not dis:
            final_text = "кава"

        print(final_text)

    return wrapper

@coffee_decorator
def coffee():
    print('кава')

coffee(milk=1, suger=1, double=False)

































