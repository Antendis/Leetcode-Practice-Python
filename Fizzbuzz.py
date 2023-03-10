#fizzbuzz --> 1-100 if less divisible by 3 then fizz, if divisible by 5 then buzz, if both then fizzbuzz
#initialise count
count = 0
#loop until counted to 100
while count < 100:
    count+=1
    #if the remainder is 0, it is divisible and acts accordingly
    if (count%3 == 0 and count%5 != 0):
        print("fizz")
    elif (count%5 == 0 and count%3 != 0):
        print("buzz")
    elif (count%3 == 0 and count%5 == 0):
        print("fizzbuzz")
    else:
        print(count)
