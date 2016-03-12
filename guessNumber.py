import random
import os
number = [0,1,2,3,4,5,6,7,8,9]
user_number_list1 = []
A_list = []
B_list = []
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
    os.system('cls')
    play_game = input("Enter 1 to play the game :")    
    if play_game == '1':        
        confrim_number = 1
        while(confrim_number):
            os.system('cls')
            A = 0
            B = 0
           
            for item in user_number_list1:
                x = user_number_list1.index(item)
                print(item,"  ",A_list[x],"A","  ",B_list[x],"B")                
            print(' ')   
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
            user_number_list1.append(user_number)
            A_list.append(A)
            B_list.append(B)
            if A == 4:
                confrim_number = 0
                print("You win the game by using",len(A_list),"times!!!!!!")
                del user_number_list1[ : ]
                del A_list[ : ]
                del B_list[ : ]                
            print(A,'A',B,'B')            
            os.system('pause')
                
                
        
    
