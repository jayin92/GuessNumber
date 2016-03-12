import random
import os
number = [0,1,2,3,4,5,6,7,8,9]
A = 0
B = 0
while(1):
    number = [0,1,2,3,4,5,6,7,8,9]
    number1 = random.choice(number)
    number.remove(number1)
    number2 = random.choice(number)
    number.remove(number2)
    number3 = random.choice(number)
    number.remove(number3)
    number4 = random.choice(number)
    number.remove(number4)
    guess_number = [number1, number2, number3, number4]    
    print(guess_number)
    play_game = input("Enter 1 to play the game :")    
    if play_game == '1':        
        confrim_number = 1
        while(confrim_number):
            os.system('cls')
            A = 0
            B = 0
            user_number  = input("Please enter the number you want to guess(4 numbers)(Each number must different) :")
            user_number_list = list(user_number)
            user_number_list = list(map(int, user_number_list))            
            for x in range(0,4):
                if user_number_list[x] in guess_number:
                    status_number = 1
                    if guess_number.index(user_number_list[x]) == x:
                        A = A + 1
                        status_number = 0
                    if status_number :
                        B = B + 1
            confrim_number = 1
            if A == 4:
                confrim_number = 0
                print("You win the game!!!!!!")
            print(A,'A',B,'B')
            os.system('pause')
                
                
        
    
