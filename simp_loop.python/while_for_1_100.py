# while loop - user input the number while (1<=x<=100)  this condition not satisfy ,  if this condition will be satisfy then loop wii be stop

# x=0
# while not (1<=x<=100):
#     x=int(input("Enter the num between 1 to  100: "))
# print("valid number",x)

5

# for loop - user input the number while (1<=x<=100)  this condition not satisfy ,  when condition will be satisfy then loop wii be stop by using BREAK 
# this loop for 4 time not infinite....
for x in range(4):
    x=int(input("Enter the num between 1 to 100: "))
    if 1<=x<=100:
        print("valid num",x)
        break
    else:
        print("Invalid number,Try again")