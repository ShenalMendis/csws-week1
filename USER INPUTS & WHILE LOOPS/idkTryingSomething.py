loop = True

tall = {}
short = {}
permitted = {}

while loop:
    
    name = input("Name: ")
    height = input("Height: ")
    height = int(height)

    if height >= 40:
        print("Too tall for the ride!")
        tall[name] = height
    
    elif 20 <= height < 40:
        print("Go Ahead!")
        permitted[name] = height
        loop = False
    
    else:
        print("Too short!") 
        short[name] = height


print(f"\nPermitted: {permitted}")
print(f"Tall: {tall}")
print(f"Short: {short}")