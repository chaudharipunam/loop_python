# loop is infinite but when we used of BREAK keyword, now it's not infinite loop

i=0
while True:
    print("the value of i is",i)
    i+=1
    if i>0:
        break