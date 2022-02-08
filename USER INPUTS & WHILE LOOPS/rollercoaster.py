from sqlalchemy import false, true

loop = True

while loop:
    
    height = input("Height: ")
    height = int(height)

    if height >= 40:
        print("Too tall for the ride!")
    elif 20 <= height < 40:
        print("Go Ahead!")
        loop = False
    else:
        print("Too short!") 