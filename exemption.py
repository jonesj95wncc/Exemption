import math
while True: 
    number = input("Please enter at positive integer: ") 
    try: 
        value = int(number) 
        print('The square root of' , value, 'is ', math.sqrt(value)) 
        break         
    except ValueError: 
        print('You can not get take the square root of a negative number')     
