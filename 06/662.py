# def fibo():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# N = 10
# fibon = fibo()
# for _ in range(N):
#     print(next(fibon))


# def make_counter():
#     x =5
#     def inner (y = 8):
#         res = x + y
#         return res
#     return inner
#
#
#
#
# counter = make_counter()
# print(counter())




# def logger(func):
#     def wrapper(*args,**kwargs):
#         gen = func(*args,**kwargs)
#         for i in gen:
#             print(f"[LOG] Вернулось число: {i}")
#             yield i
#     return wrapper
#
#
# @logger
# def counter_up_to(N):
#     count = 1
#     for _ in range(N):
#         yield  count
#         count+=1
#
#
# c = counter_up_to(5)
# for x in c:
#     print(x)


# def make_power(n):
#     def inner(y):
#         return n ** y
#     return inner
#
#
# square = make_power(2)
#
# print(square(4))

# def make_limited_counter(n):
#     count = 0
#     def inner ():
#         nonlocal count
#         count += 1
#         if count <= n:
#             return count
#         else:
#             return "Достигнут лимит!"
#
#     return inner
#
# counter = make_limited_counter(3)
# print(counter())  # 1
# print(counter())  # 2
# print(counter())  # 3
# print(counter())  # "Достигнут лимит!"
# print(counter())  # "Достигнут лимит!"
#




# def repeat_limit(n):
#     def decorator(func):
#         count = 0
#         def wrapper(*args,**kwargs):
#             nonlocal count
#             count+=1
#             if count <= n:
#                 return func(*args,**kwargs)
#             else:
#                 return "Превышен лимит вызовов!"
#
#         return wrapper
#     return decorator
#
# @repeat_limit(3)
# def greet(name):
#     return f"Привет, {name}!"
#
# print(greet("Аня"))  # Привет, Аня!
# print(greet("Боб"))  # Привет, Боб!
# print(greet("Кирилл"))  # Привет, Кирилл!
# print(greet("Даша"))   # "Превышен лимит вызовов!"
# print(greet("Ева"))



# def logger(func):
#     def wrapper(*args,**kwargs):
#         gen = func(*args,**kwargs)
#         for number in gen:
#             print(f"[LOG] Сгенерировано число: {number}")
#             yield number
#     return wrapper
#
# @logger
# def even_numbers(limit):
#     n = 0
#     while n <= limit:
#         if n % 2 == 0:
#             yield n
#         n += 1
#
# evens = even_numbers(6)
# for num in evens:
#     print("Используем число:", num)
































