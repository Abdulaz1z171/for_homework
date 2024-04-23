# def addNumbers(a:int,b:int):
#     return a+b


# import you_tube_exemples
# print(you_tube_exemples.multiplication(8,8))


# help('modules')


#  walrus (:=) print(apple := 'apple) faqat true qiymat saqlaydi

# foods = list()
# while food := input('What food do you like? ') != 'quite':
#     foods.append(food)
# else:
#     print(foods)


# /////////////////////////////////////////
#  functions to variebles 

# say = print
# say('hello world')
# hello world

"""

higher order function bunda funksiya argumentiga funksiya berish mumkin
"""
"""
def loud(text):
    return text.upper()
def quite(text):
    return text.lower() 

def hello(func):
    text = func(input('>>>>>>>>'))
    print(text)

hello(loud)
hello(quite)
"""

# ////////////////////////////////////////
# 2 nd version higher order function

"""
dividend = bo'linuvchi
divisor  = bo'luvchi
quotient = bo'linma
"""

def divisor(x:int):
    def dividend(y:int):
        return y/x
    return dividend


devide = divisor(2)
print(devide(5))
