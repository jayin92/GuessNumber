import random

def random_number_function():
    number = [0,1,2,3,4,5,6,7,8,9]    
    number1 = random.choice(number)
    number.remove(number1)
    number2 = random.choice(number)
    number.remove(number2)
    number3 = random.choice(number)
    number.remove(number3)
    number4 = random.choice(number)
    number.remove(number4)
    random_number_function.guess_number = [number1, number2, number3, number4]
    
