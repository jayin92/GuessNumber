from Random_number import random_number_function
import random

guess_number = []
imNumber = []
while(1):
    random_number_function()
    for item in random_number_function.guess_number:
        guess_number.append(item)
        status_number = 1
    while(status_number):
        print("I guess",guess_number)
        user_AABB = list(input("Enter xAxB, for example: 1A2B :"))
        user_AABB.remove('A')
        user_AABB.remove('B')
        #print(user_AABB)
        user_AABB = list(map(int, user_AABB)
        if user_AABB[0] == 0 && user_AABB[1] == 0:
            for item in guess_number:
                inNumber.append(item)
                random_number_function()
    			for item in random_number_function.guess_number:
        			guess_number.append(item)
        if user_AABB[1] > 0:
        	random.shuffle(guess_number)
